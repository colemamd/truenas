"""Constants for the TrueNAS integration."""

from homeassistant.components import truenas

from homeassistant.const import (
    DATA_MEGABYTES,
    DATA_RATE_KILOBYTES_PER_SECOND,
    PERCENTAGE,
)

from aiotruenas_client import CachingMachine as TrueNASMachine

DOMAIN = "truenas"

ENTITY_NAME = "name"
ENTITY_UNIT = "unit"
ENTITY_ICON = "icon"
ENTITY_CLASS = "device_class"
ENTITY_ENABLE = "enable"

# Sensors
UTILISATION_SENSORS = {
    f"{TrueNASMachine}:cpu_other_load": {
        ENTITY_NAME: "CPU Load (Other)",
        ENTITY_UNIT: PERCENTAGE,
        ENTITY_ICON: "mdi:chip",
        ENTITY_CLASS: None,
        ENTITY_ENABLE: False,
    },
    f"{TrueNASMachine}:cpu_user_load": {
        ENTITY_NAME: "CPU Load (User)",
        ENTITY_UNIT: PERCENTAGE,
        ENTITY_ICON: "mdi:chip",
        ENTITY_CLASS: None,
        ENTITY_ENABLE: True,
    },
    f"{TrueNASMachine}:cpu_system_load": {
        ENTITY_NAME: "CPU Load (System)",
        ENTITY_UNIT: PERCENTAGE,
        ENTITY_ICON: "mdi:chip",
        ENTITY_CLASS: None,
        ENTITY_ENABLE: False,
    },
    f"{TrueNASMachine}:cpu_total_load": {
        ENTITY_NAME: "CPU Load (Total)",
        ENTITY_UNIT: PERCENTAGE,
        ENTITY_ICON: "mdi:chip",
        ENTITY_CLASS: None,
        ENTITY_ENABLE: True,
    },
    f"{TrueNASMachine}:cpu_1min_load": {
        ENTITY_NAME: "CPU Load (1 min)",
        ENTITY_UNIT: PERCENTAGE,
        ENTITY_ICON: "mdi:chip",
        ENTITY_CLASS: None,
        ENTITY_ENABLE: False,
    },
    f"{TrueNASMachine}:cpu_5min_load": {
        ENTITY_NAME: "CPU Load (5 min)",
        ENTITY_UNIT: PERCENTAGE,
        ENTITY_ICON: "mdi:chip",
        ENTITY_CLASS: None,
        ENTITY_ENABLE: True,
    },
    f"{TrueNASMachine}:cpu_15min_load": {
        ENTITY_NAME: "CPU Load (15 min)",
        ENTITY_UNIT: PERCENTAGE,
        ENTITY_ICON: "mdi:chip",
        ENTITY_CLASS: None,
        ENTITY_ENABLE: True,
    },
    f"{TrueNASMachine}:memory_real_usage": {
        ENTITY_NAME: "Memory Usage (Real)",
        ENTITY_UNIT: PERCENTAGE,
        ENTITY_ICON: "mdi:memory",
        ENTITY_CLASS: None,
        ENTITY_ENABLE: True,
    },
    f"{TrueNASMachine}:memory_size": {
        ENTITY_NAME: "Memory Size",
        ENTITY_UNIT: DATA_MEGABYTES,
        ENTITY_ICON: "mdi:memory",
        ENTITY_CLASS: None,
        ENTITY_ENABLE: False,
    },
    f"{TrueNASMachine}:memory_cached": {
        ENTITY_NAME: "Memory Cached",
        ENTITY_UNIT: DATA_MEGABYTES,
        ENTITY_ICON: "mdi:memory",
        ENTITY_CLASS: None,
        ENTITY_ENABLE: False,
    },
    f"{TrueNASMachine}:memory_available_swap": {
        ENTITY_NAME: "Memory Available (Swap)",
        ENTITY_UNIT: DATA_MEGABYTES,
        ENTITY_ICON: "mdi:memory",
        ENTITY_CLASS: None,
        ENTITY_ENABLE: True,
    },
    f"{TrueNASMachine}:memory_available_real": {
        ENTITY_NAME: "Memory Available (Real)",
        ENTITY_UNIT: DATA_MEGABYTES,
        ENTITY_ICON: "mdi:memory",
        ENTITY_CLASS: None,
        ENTITY_ENABLE: True,
    },
    f"{TrueNASMachine}:memory_total_swap": {
        ENTITY_NAME: "Memory Total (Swap)",
        ENTITY_UNIT: DATA_MEGABYTES,
        ENTITY_ICON: "mdi:memory",
        ENTITY_CLASS: None,
        ENTITY_ENABLE: True,
    },
    f"{TrueNASMachine}:memory_total_real": {
        ENTITY_NAME: "Memory Total (Real)",
        ENTITY_UNIT: DATA_MEGABYTES,
        ENTITY_ICON: "mdi:memory",
        ENTITY_CLASS: None,
        ENTITY_ENABLE: True,
    },
    f"{TrueNASMachine}:network_up": {
        ENTITY_NAME: "Network Up",
        ENTITY_UNIT: DATA_RATE_KILOBYTES_PER_SECOND,
        ENTITY_ICON: "mdi:upload",
        ENTITY_CLASS: None,
        ENTITY_ENABLE: True,
    },
    f"{TrueNASMachine}:network_down": {
        ENTITY_NAME: "Network Down",
        ENTITY_UNIT: DATA_RATE_KILOBYTES_PER_SECOND,
        ENTITY_ICON: "mdi:download",
        ENTITY_CLASS: None,
        ENTITY_ENABLE: True,
    },
}
