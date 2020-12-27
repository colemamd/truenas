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

from . import TrueNASMachine

from .const import (
    DOMAIN,
    UTILISATION_SENSORS,
)


async def async_setup_entry(
    hass: HomeAssistantType, entry: ConfigEntry, async_add_entities
) -> None:
    """Set up the TrueNAS Sensor."""

    api = hass.data[DOMAIN][entry.unique_id][TrueNASMachine]

    entities = [
        api(sensor_type, UTILISATION_SENSORS[sensor_type])
        for sensor_type in UTILISATION_SENSORS
    ]

    async_add_entities(entities)
