"""Config flow for TrueNAS integration."""
import logging

import voluptuous as vol

from homeassistant import config_entries, core, exceptions
from homeassistant.core import callback

from .const import DOMAIN  # pylint:disable=unused-import

_LOGGER = logging.getLogger(__name__)

STEP_USER_DATA_SCHEMA = vol.Schema({"host": str, "username": str, "password": str})


class TrueNASConfigHub:
    """Placeholder class to make tests pass.

    TODO Remove this placeholder class and replace with things from your PyPI package.
    """

    def __init__(self, host):
        """Initialize."""
        self.host = host

    async def authenticate(self, username, password) -> bool:
        """Test if we can authenticate with the host."""
        return True


async def validate_input(hass: core.HomeAssistant, data):
    """Validate the user input allows us to connect.

    Data has the keys from STEP_USER_DATA_SCHEMA with values provided by the user.
    """
 
    hub = TrueNASConfigHub(data["host"])

    if not await hub.authenticate(data["username"], data["password"]):
        raise InvalidAuth

    # Return info that you want to store in the config entry.
    return {"title": "TrueNAS"}


class TrueNASFlowHandler(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for TrueNAS."""

    VERSION = 1
    CONNECTION_CLASS = config_entries.CONN_CLASS_LOCAL_POLL

    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
      """Get the options flow for this handler."""
      return TrueNASOptionsFlowHandler(config_entry)

    def __init__(self):
        """Initialize the TrueNAS config flow."""
        self.saved_user_input = {}

    async def _show_setup_form(self, user_input=None, errors=None):
      """Show setup form to the user"""
      if not user_input:
        user_input = {}

      step_id = "user"

      return self.async_show_form(
        step_id=step_id,
        data_schema=data_schema,
        errors=errors or {},
      )

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        if user_input is None:
            return self.async_show_form(
                step_id="init", data_schema=STEP_USER_DATA_SCHEMA
            )

        errors = {}

        try:
            info = await validate_input(self.hass, user_input)
        except CannotConnect:
            errors["base"] = "cannot_connect"
        except InvalidAuth:
            errors["base"] = "invalid_auth"
        except Exception:  # pylint: disable=broad-except
            _LOGGER.exception("Unexpected exception")
            errors["base"] = "unknown"
        else:
            return self.async_create_entry(title=info["title"], data=user_input)

        return self.async_show_form(
            step_id="init", data_schema=STEP_USER_DATA_SCHEMA, errors=errors
        )


class TrueNASOptionsFlowHandler(config_entries.OptionsFlow):
    """Handle an option flow."""

    def __init__(self, config_entry):
        """Initialize options flow."""
        self.config_entry = config_entry

    async def async_step_init(self, user_input=None):
        """Handle options flow."""
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)

        return self.async_show_form(step_id="init", data_schema=STEP_USER_DATA_SCHEMA)
class CannotConnect(exceptions.HomeAssistantError):
    """Error to indicate we cannot connect."""


class InvalidAuth(exceptions.HomeAssistantError):
    """Error to indicate there is invalid auth."""
