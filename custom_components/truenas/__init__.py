"""The TrueNAS integration."""
import asyncio
from custom_components.truenas.config_flow import STEP_USER_DATA_SCHEMA

import voluptuous as vol

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import HomeAssistantType

from .const import DOMAIN

from aiotruenas_client import CachingMachine as TrueNASMachine

PLATFORMS = ["sensor"]

async def async_setup(hass, config):
    """Set up the TrueNAS component."""
    return True


async def async_setup_entry(hass: HomeAssistantType, entry: ConfigEntry):
    """Set up TrueNAS from a config entry."""

    for component in PLATFORMS:
        hass.async_create_task(
            hass.config_entries.async_forward_entry_setup(entry, component)
        )

    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.unique_id] = {
        TrueNASMachine: api,
    }

    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Unload a config entry."""
    unload_ok = all(
        await asyncio.gather(
            *[
                hass.config_entries.async_forward_entry_unload(entry, platform)
                for platform in PLATFORMS
            ]
        )
    )
    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id)

    return unload_ok

class TruenasApi:
  """Class to interface with TrueNAS websocket API."""

def __init__(self, hass: HomeAssistantType, entry: ConfigEntry):
  """Initialize the wrapper class."""
  self._hass = hass
  self._entry = entry

  api = TrueNASMachine(hass, entry)

  #TrueNAS API
  self.disks = api.get_disks()
  self.pools = api.get_pools()
  self.vms = api.get_vms()