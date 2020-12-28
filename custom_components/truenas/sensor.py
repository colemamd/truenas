"""Support for TrueNAS sensors."""
from datetime import timedelta
import logging

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import (
    CONF_DISKS,
    DATA_MEGABYTES,
    DATA_RATE_KILOBYTES_PER_SECOND,
    DATA_TERABYTES,
    PRECISION_TENTHS,
    TEMP_CELSIUS,
)
from homeassistant.helpers.temperature import display_temp
from homeassistant.helpers.typing import HomeAssistantType
from homeassistant.util.dt import utcnow

from . import TrueNASMachine, TruenasApi

from .const import (
    DOMAIN,
    UTILISATION_SENSORS,
)


async def async_setup_entry(
    hass: HomeAssistantType, entry: ConfigEntry, async_add_entities
) -> None:
    """Set up the TrueNAS Sensor."""

    entities = [
        api(sensor_type, UTILISATION_SENSORS[sensor_type])
        for sensor_type in UTILISATION_SENSORS
    ]

    async_add_entities(entities)

class TrueNASDiskSensor(Entity):
  """Base class for a TrueNAS Disk sensor."""

  def __init__(self, api):
    """Initialize the sensor."""
    self._api = TruenasApi.get_disks()

class TrueNASPoolSensor(TrueNASSensor):
  """Base class for a TrueNAS Pool sensor."""

  def __init__(self, api):
    """Initialize the sensor."""
    self._api = TruenasApi.get_pools()

  @property
  def state(self):
    """Return the state of the sensor."""

class TrueNASVMSensor(TrueNASSensor):
  """Base class for a TrueNAS VM sensor."""

  def __init__(self, api):
    """Initiliaze the sensor."""
    self._api = TruenasApi.get_vms()

  @property
  def state(self):
    """Return the state of the sensor."""
