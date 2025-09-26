# NEON AI (TM) SOFTWARE, Software Development Kit & Application Development System
# All trademark and other rights reserved by their respective owners
# Copyright 2008-2025 NeonGecko.com Inc.
# BSD-3
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 1. Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
# 3. Neither the name of the copyright holder nor the names of its
#    contributors may be used to endorse or promote products derived from this
#    software without specific prior written permission.
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
# THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
# PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR
# CONTRIBUTORS  BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA,
# OR PROFITS;  OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE,  EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
import os
from time import time
from typing import List, Optional

from neon_data_models.models.api.llm import (
    LLMPersona,
    LLMPersonaIdentity,
)

from neon_mq_connector.utils import RepeatingTimer
from neon_mq_connector.utils.client_utils import send_mq_request
from neon_utils.logger import LOG
from pydantic import ValidationError

from neon_llm_core.utils.constants import LLM_VHOST
from neon_llm_core.utils.personas.state import PersonaHandlersState


class PersonasProvider:
    """
    Manages personas defined via Klat. Each LLM that connects to the MQ bus will
    include an instance of this object to track changes to personas.
    """

    PERSONA_STATE_TTL = int(os.getenv("PERSONA_STATE_TTL", 15 * 60))
    PERSONA_SYNC_INTERVAL = int(os.getenv("PERSONA_SYNC_INTERVAL", 0))
    GET_CONFIGURED_PERSONAS_QUEUE = "get_configured_personas"

    def __init__(self, service_name: str, ovos_config: dict):
        self.service_name = service_name
        self._persona_handlers_state = PersonaHandlersState(service_name=service_name,
                                                            ovos_config=ovos_config)
        self._personas = []  # list of personas available for given service
        self._persona_last_sync = 0
        self._persona_sync_thread = None

    @property
    def persona_sync_thread(self) -> RepeatingTimer:
        """Creates new synchronization thread which fetches Klat personas"""
        if not (isinstance(self._persona_sync_thread, RepeatingTimer) and
                self._persona_sync_thread.is_alive()):
            self._persona_sync_thread = RepeatingTimer(self.PERSONA_SYNC_INTERVAL,
                                                       self._fetch_persona_config)
            self._persona_sync_thread.daemon = True
        return self._persona_sync_thread

    @property
    def personas(self) -> List[LLMPersona]:
        return self._personas

    @personas.setter
    def personas(self, data: List[LLMPersona]):
        LOG.debug(f'Setting personas={data}')
        if self._should_reset_personas(data=data):
            LOG.warning(f'Persona state expired, setting default personas')
            self._personas = []
            self._persona_handlers_state.init_default_personas()
        else:
            self._personas = data
            self._persona_handlers_state.clean_up_personas(ignore_items=self._personas)

    def _should_reset_personas(self, data: List[LLMPersona]) -> bool:
        """
        Checks if personas should be re-initialized after setting a new value
        for personas.

        If PERSONA_SYNC_INTERVAL is enabled - verifies based on TTL, otherwise

        :param data: requested list of personas
        :return: True if requested `data` should be ignored and personas
            reloaded from config, False if requested `data` should be used
            directly
        """
        return self._should_reset_personas_based_on_ttl(data) if self.PERSONA_SYNC_INTERVAL > 0 else not data

    def _should_reset_personas_based_on_ttl(self, data: dict) -> bool:
        """
        Determines whether personas should be reset based on Time-to-Live (TTL) and
        the synchronization timestamp.

        Examines the time elapsed since the last persona synchronization in relation
        to a predefined TTL. Also considers whether the state of the personas and the
        incoming data indicate a need for resetting.

        :param data: provided persona data

        returns: True if personas need to be reset based on TTL False otherwise.
        """
        return (not (self._persona_last_sync == 0 and data)
                and int(time()) - self._persona_last_sync > self.PERSONA_STATE_TTL)

    def _fetch_persona_config(self):
        """
        Get personas from a provider on the MQ bus and update the internal
        `personas` reference.
        """
        response = send_mq_request(
            vhost=LLM_VHOST,
            request_data={"service_name": self.service_name},
            target_queue=PersonasProvider.GET_CONFIGURED_PERSONAS_QUEUE,
            timeout=60)
        self.parse_persona_config_response(response)

    def parse_persona_config_response(self, persona_response: dict):
        """
        Parses and processes a response containing persona data, updates internal state,
        and manages personas accordingly.

        :param persona_response: A dictionary containing the response data with
                                 persona information.
                                 Expected to contain a key 'items' holding a list of
                                 persona details.
        """
        if 'items' in persona_response:
            self._persona_last_sync = int(time())
        response_data = persona_response.get('items', [])
        active_personas = []
        for persona_data in response_data:
            applied_persona = self.apply_persona_data(persona_data=persona_data)
            if applied_persona:
                active_personas.append(applied_persona)
        self.personas = active_personas

    def apply_persona_data(self, persona_data: dict) -> Optional[LLMPersona]:
        """
        Validates and applies persona data.

        Takes a dictionary representing persona data, validates it,
        and applies the validated persona to the current instance.
        If the validation succeeds, it returns the applied persona. Otherwise, returns None.

        :param persona_data: Dictionary containing persona data

        :returns: The validated and applied persona instance if validation is successful, or None otherwise.
        """
        validated_persona = self._validate_persona_data(persona_data)
        if validated_persona:
            persona_added = self._add_persona(persona=validated_persona)
            if persona_added:
                return validated_persona

    @staticmethod
    def _validate_persona_data(persona_data: dict) -> Optional[LLMPersona]:
        """
        Validates of the persona data and returns the resulting `PersonaModel`.
        If validation fails - logs error and returns None

        :param persona_data : A dictionary containing details of the persona, where
                              specific key-value mappings are applied for validation.

        returns: A validated and updated `PersonaModel` instance based on the provided data if
                 validation was successful, None otherwise
        """
        persona_data.setdefault('name', persona_data.pop('persona_name', None))

        try:
            return LLMPersona.model_validate(obj=persona_data)
        except ValidationError as err:
            LOG.error(f"Failed to apply persona data from {persona_data} - {str(err)}")
            return

    @staticmethod
    def _validate_persona_identity(persona_identity_data: dict) -> Optional[LLMPersonaIdentity]:
        """
        Validates of the persona data and returns the resulting `PersonaModel`.
        If validation fails - logs error and returns None

        :param persona_identity_data : A dictionary containing details of the persona identity, where
                                       specific key-value mappings are applied for validation.

        returns: A validated and updated `LLMPersonaIdentity` instance based on the provided data if
                 validation was successful, None otherwise
        """
        persona_identity_data.setdefault('name', persona_identity_data.pop('persona_name', None))

        try:
            return LLMPersonaIdentity.model_validate(obj=persona_identity_data)
        except ValidationError as err:
            LOG.error(f"Failed to apply persona identity data from {persona_identity_data} - {str(err)}")
            return

    def _add_persona(self, persona: LLMPersona) -> bool:
        """
        Attempts to add incoming persona and return an updated PersonaModel instance if successful.
        If default personas are running upon adding persona - removes default personas.
        If state container has only one running persona & it was disabled by this method -
        triggers initialisation of the default personas.

        :param persona: `LLMPersona` instance to add to the `PersonaHandlersState` container

        :returns: True if incoming persona object in case of successful addition or if identical persona already exists
                  False otherwise
        """

        new_persona = self._persona_handlers_state.add_persona_handler(persona=persona)

        if new_persona:
            LOG.info(f"Persona {persona.id} updated successfully")

            # Once first manually configured persona added - pruning default personas
            if self._persona_handlers_state.default_personas_running:
                LOG.info("Starting to remove default personas")
                self._persona_handlers_state.clean_up_personas(ignore_items=[persona])
                self._persona_handlers_state.default_personas_running = False
                LOG.info("Completed removing of default personas")

        elif persona.id not in self._persona_handlers_state.connected_persona_ids:
            # May occur if the last updated persona was set to be disabled
            if not self._persona_handlers_state.has_connected_personas():
                LOG.info("No personas connected after the last update - setting default personas")
                self._persona_handlers_state.init_default_personas()
            return False

        return True

    def remove_persona(self, persona_data: dict):
        """
        Removes a persona from the active persona handlers state.

        This method handles the removal of a persona based on persona data.
        It ensures that the default personas are initialized if no other connected personas
        remain after the removal.

        :param persona_data: A dictionary containing details of the persona to be removed.
        """
        if (self._persona_handlers_state.has_connected_personas() and
                not self._persona_handlers_state.default_personas_running):
            persona_identity = self._validate_persona_identity(persona_identity_data=persona_data)
            if persona_identity:
                self._persona_handlers_state.remove_persona(persona_id=persona_identity.id)
                LOG.info(f"Persona {persona_identity.id} removed successfully")
                if not self._persona_handlers_state.has_connected_personas():
                    LOG.info("No personas connected after the last removal - setting default personas")
                    self._persona_handlers_state.init_default_personas()
        else:
            LOG.warning("No running personas detected - skipping persona removal")

    def start_sync(self):
        """
        Update personas and start thread to periodically update from a service
        on the MQ bus.
        """
        self._fetch_persona_config()
        if self.PERSONA_SYNC_INTERVAL > 0:
            self.persona_sync_thread.start()

    def stop_sync(self):
        """
        Stop persona updates from the MQ bus.
        """
        if self._persona_sync_thread:
            self._persona_sync_thread.cancel()
            self._persona_sync_thread = None
