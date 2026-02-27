import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import (
    uart,
    sensor,
    switch,
    select,
    number,
    climate,
    text_sensor,
)
from esphome.const import (
    CONF_ID,
    DEVICE_CLASS_TEMPERATURE,
    STATE_CLASS_MEASUREMENT,
    STATE_CLASS_TOTAL_INCREASING,
    DEVICE_CLASS_ENERGY,
    DEVICE_CLASS_POWER,
    DEVICE_CLASS_HUMIDITY,
    DEVICE_CLASS_VOLTAGE,
    DEVICE_CLASS_CURRENT,
    UNIT_CELSIUS,
    UNIT_PERCENT,
    UNIT_WATT,
    UNIT_VOLT,
    UNIT_AMPERE,
    CONF_UNIT_OF_MEASUREMENT,
    CONF_DEVICE_CLASS,
    CONF_FILTERS,
    CONF_FLOW_CONTROL_PIN,
    ENTITY_CATEGORY_DIAGNOSTIC,
)
from esphome.core import CORE, Lambda
from esphome.cpp_helpers import gpio_pin_expression
from esphome import pins

CODEOWNERS = ["matthias882", "lanwin", "omerfaruk-aran"]
DEPENDENCIES = ["uart"]
AUTO_LOAD = ["sensor", "switch", "select", "number", "climate", "text_sensor"]
MULTI_CONF = False

CONF_SAMSUNG_AC_ID = "samsung_ac_id"

samsung_ac = cg.esphome_ns.namespace("samsung_ac")
Samsung_AC = samsung_ac.class_("Samsung_AC", cg.PollingComponent, uart.UARTDevice)
Samsung_AC_Device = samsung_ac.class_("Samsung_AC_Device")
Samsung_AC_Switch = samsung_ac.class_("Samsung_AC_Switch", switch.Switch)
Samsung_AC_Mode_Select = samsung_ac.class_("Samsung_AC_Mode_Select", select.Select)
Samsung_AC_Water_Heater_Mode_Select = samsung_ac.class_(
    "Samsung_AC_Water_Heater_Mode_Select", select.Select
)
Samsung_AC_Generic_Select = samsung_ac.class_(
    "Samsung_AC_Generic_Select", select.Select
)
Samsung_AC_Number = samsung_ac.class_("Samsung_AC_Number", number.Number)
Samsung_AC_Climate = samsung_ac.class_("Samsung_AC_Climate", climate.Climate)

# not sure why select.select_schema did not work yet
SELECT_MODE_SCHEMA = select.select_schema(Samsung_AC_Mode_Select)
SELECT_WATER_HEATER_MODE_SCHEMA = select.select_schema(
    Samsung_AC_Water_Heater_Mode_Select
)

SELECT_GENERIC_SCHEMA = select.select_schema(Samsung_AC_Generic_Select)

NUMBER_SCHEMA = number.number_schema(Samsung_AC_Number).extend(
    {cv.GenerateID(): cv.declare_id(Samsung_AC_Number)}
)

CLIMATE_SCHEMA = climate.climate_schema(Samsung_AC_Climate)

CONF_DEVICE_ID = "samsung_ac_device_id"
CONF_DEVICE_ADDRESS = "address"
CONF_DEVICE_ROOM_TEMPERATURE = "room_temperature"
CONF_DEVICE_ROOM_TEMPERATURE_OFFSET = "room_temperature_offset"
CONF_DEVICE_TARGET_TEMPERATURE = "target_temperature"
CONF_DEVICE_WATER_OUTLET_TARGET = "water_outlet_target"
CONF_DEVICE_OUTDOOR_TEMPERATURE = "outdoor_temperature"
CONF_DEVICE_INDOOR_EVA_IN_TEMPERATURE = "indoor_eva_in_temperature"
CONF_DEVICE_INDOOR_EVA_OUT_TEMPERATURE = "indoor_eva_out_temperature"
CONF_DEVICE_WATER_TEMPERATURE = "water_temperature"
CONF_DEVICE_WATER_TARGET_TEMPERATURE = "water_target_temperature"
CONF_DEVICE_POWER = "power"
CONF_DEVICE_AUTOMATIC_CLEANING = "automatic_cleaning"
CONF_DEVICE_WATER_HEATER_POWER = "water_heater_power"
CONF_DEVICE_MODE = "mode"
CONF_DEVICE_WATER_HEATER_MODE = "water_heater_mode"
CONF_DEVICE_CLIMATE = "climate"
CONF_DEVICE_ROOM_HUMIDITY = "room_humidity"
CONF_DEVICE_CUSTOM = "custom_sensor"
CONF_DEVICE_CUSTOM_MESSAGE = "message"
CONF_DEVICE_CUSTOM_RAW_FILTERS = "raw_filters"
CONF_DEVICE_ERROR_CODE = "error_code"
CONF_DEVICE_OUT_CONTROL_WATTMETER_ALL_UNIT_ACCUM = "outdoor_instantaneous_power"
CONF_DEVICE_OUT_CONTROL_WATTMETER_1W_1MIN_SUM = "outdoor_cumulative_energy"
CONF_DEVICE_OUT_SENSOR_CT1 = "outdoor_current"
CONF_DEVICE_OUT_SENSOR_VOLTAGE = "outdoor_voltage"
CONF_MAP_AUTO_TO_HEAT_COOL = "map_auto_to_heat_cool"
CONF_DEBUG_LOG_MESSAGES_ON_CHANGE = "debug_log_messages_on_change"
CONF_NON_NASA_TX_DELAY_MS = "non_nasa_tx_delay_ms"

CONF_CAPABILITIES = "capabilities"
CONF_CAPABILITIES_FAN_MODES = "fan_modes"
CONF_CAPABILITIES_HORIZONTAL_SWING = "horizontal_swing"
CONF_CAPABILITIES_VERTICAL_SWING = "vertical_swing"

CONF_PRESETS = "presets"
CONF_PRESET_NAME = "name"
CONF_PRESET_ENABLED = "enabled"
CONF_PRESET_VALUE = "value"

CONF_DEVICE_OUT_OPERATION_ODU_MODE_TEXT = "outdoor_operation_odu_mode"
CONF_DEVICE_OUT_OPERATION_HEATCOOL_TEXT = "outdoor_operation_heatcool"

CONF_DEVICE_EVA_IN_TEMP = "eva_in_temp"
CONF_DEVICE_EVA_OUT_TEMP = "eva_out_temp"
CONF_DEVICE_PHE_OUT_WATER_OUT = "phe_out_water_out"
CONF_DEVICE_PHE_IN_WATER_RETURN = "phe_in_water_return"
CONF_DEVICE_WATER_FLOW = "water_flow"
CONF_DEVICE_DHW_VALVE_DIRECTION = "dhw_valve_direction"
CONF_DEVICE_DHW_DISINFECTION_DAY = "dhw_disinfection_day"
CONF_DEVICE_DHW_DISINFECTION_START_TIME = "dhw_disinfection_start_time"
CONF_DEVICE_DHW_DISINFECTION_TARGET_TEMP = "dhw_disinfection_target_temp"
CONF_DEVICE_DHW_DISINFECTION_DURATION = "dhw_disinfection_duration"
CONF_DEVICE_DHW_DISINFECTION_MAX_TIME = "dhw_disinfection_max_time"
CONF_DEVICE_SILENCE_MODE = "silence_mode"
CONF_DEVICE_WATER_LAW_TARGET_FLOW_TEMP = "water_law_target_flow_temp"
CONF_DEVICE_WATER_LAW_TARGET_TEMP_SHIFT = "water_law_target_temp_shift"
CONF_DEVICE_WATER_PUMP_STATUS = "water_pump_status"
CONF_DEVICE_INDOOR_POWER_CONSUMPTION = "indoor_power_consumption"
CONF_DEVICE_GENERATED_POWER_LAST_MINUTE = "generated_power_last_minute"
CONF_DEVICE_DEFROST_STATUS = "defrost_status"
CONF_DEVICE_BOOSTER_HEATER_STATUS = "booster_heater_status"
CONF_DEVICE_HEATING_WATER_OUTLET_UPPER = "heating_water_outlet_temp_upper"
CONF_DEVICE_HEATING_WATER_OUTLET_LOWER = "heating_water_outlet_temp_lower"
CONF_DEVICE_HEATING_LOWER_OUTDOOR_TEMP = "heating_lower_outdoor_temp"
CONF_DEVICE_HEATING_UPPER_OUTDOOR_TEMP = "heating_upper_outdoor_temp"
CONF_DEVICE_HEATING_WATER_TEMP_COLD_OUTDOOR = "heating_water_temp_cold_outdoor"
CONF_DEVICE_HEATING_WATER_TEMP_WARM_OUTDOOR = "heating_water_temp_warm_outdoor"
CONF_DEVICE_HEATING_DHW_PRIORITY = "heating_dhw_priority"
CONF_DEVICE_HEATING_INVERTER_PUMP_APPLICATION = "heating_inverter_pump_application"
CONF_DEVICE_HEATING_INVERTER_PUMP_TARGET_DELTA = "heating_inverter_pump_target_delta"
CONF_DEVICE_DHW_TANK_TEMP_UPPER = "dhw_tank_temp_upper"
CONF_DEVICE_DHW_TANK_TEMP_LOWER = "dhw_tank_temp_lower"
CONF_DEVICE_DHW_OPERATION_MODE = "dhw_operation_mode"
CONF_DEVICE_HP_MAX_TEMP_ALONE = "hp_max_temp_alone"
CONF_DEVICE_HP_TEMP_DIFF_OFF = "hp_temp_diff_off"
CONF_DEVICE_HP_TEMP_DIFF_ON = "hp_temp_diff_on"
CONF_DEVICE_DHW_BOOSTER_HEATER = "dhw_booster_heater"
CONF_DEVICE_DHW_BOOSTER_HEATER_DELAY = "dhw_booster_heater_delay"
CONF_DEVICE_DHW_BOOSTER_HEATER_OVERSHOOT = "dhw_booster_heater_overshoot"
CONF_DEVICE_DHW_DISINFECTION_ENABLE = "dhw_disinfection_enable"
CONF_DEVICE_DHW_FORCED_OPERATION_TIMER = "dhw_forced_operation_timer"
CONF_DEVICE_DHW_FORCED_OPERATION_TIME = "dhw_forced_operation_time"
CONF_DEVICE_HEATING_PRIORITY_CHANGEOVER_TEMP = "heating_priority_changeover_temp"
CONF_DEVICE_HEATING_DHW_OFF_OUTDOOR_TEMP = "heating_dhw_off_outdoor_temp"


def preset_entry(name: str, value: int, displayName: str):
    return (
        cv.Optional(name, default=False),
        cv.Any(
            cv.boolean,
            cv.All(
                {
                    cv.Optional(CONF_PRESET_ENABLED, default=False): cv.boolean,
                    cv.Optional(CONF_PRESET_NAME, default=displayName): cv.string,
                    cv.Optional(CONF_PRESET_VALUE, default=value): cv.int_,
                }
            ),
        ),
    )


PRESETS = {
    "sleep": {"value": 1, "displayName": "Sleep"},
    "quiet": {"value": 2, "displayName": "Quiet"},
    "fast": {"value": 3, "displayName": "Fast"},
    "longreach": {"value": 6, "displayName": "LongReach"},
    "eco": {"value": 7, "displayName": "Eco"},
    "windfree": {"value": 9, "displayName": "WindFree"},
}

CAPABILITIES_SCHEMA = cv.Schema(
    {
        cv.Optional(CONF_CAPABILITIES_FAN_MODES, default=True): cv.boolean,
        cv.Optional(CONF_CAPABILITIES_HORIZONTAL_SWING, default=False): cv.boolean,
        cv.Optional(CONF_CAPABILITIES_VERTICAL_SWING, default=False): cv.boolean,
        cv.Optional(CONF_PRESETS): cv.Schema(
            dict(
                [
                    preset_entry(
                        name, PRESETS[name]["value"], PRESETS[name]["displayName"]
                    )
                    for name in PRESETS
                ]
            )
        ),
    }
)

CUSTOM_SENSOR_SCHEMA = sensor.sensor_schema().extend(
    {
        cv.Required(CONF_DEVICE_CUSTOM_MESSAGE): cv.hex_int,
    }
)


def custom_sensor_schema(
    message: int,
    unit_of_measurement=cv.UNDEFINED,
    icon=cv.UNDEFINED,
    accuracy_decimals=cv.UNDEFINED,
    device_class=cv.UNDEFINED,
    state_class=cv.UNDEFINED,
    entity_category=cv.UNDEFINED,
    raw_filters=None,
):
    if raw_filters is None:
        raw_filters = []

    schema = sensor.sensor_schema(
        unit_of_measurement=unit_of_measurement,
        icon=icon,
        accuracy_decimals=accuracy_decimals,
        device_class=device_class,
        state_class=state_class,
        entity_category=entity_category,
    ).extend(
        {
            cv.Optional(CONF_DEVICE_CUSTOM_MESSAGE, default=message): cv.hex_int,
            cv.Optional(
                CONF_DEVICE_CUSTOM_RAW_FILTERS, default=raw_filters
            ): sensor.validate_filters,
        }
    )

    return schema


def temperature_sensor_schema(message: int):
    return custom_sensor_schema(
        message=message,
        unit_of_measurement=UNIT_CELSIUS,
        accuracy_decimals=1,
        device_class=DEVICE_CLASS_TEMPERATURE,
        state_class=STATE_CLASS_MEASUREMENT,
        raw_filters=[{"lambda": Lambda("return (int16_t)x;")}, {"multiply": 0.1}],
    )


def humidity_sensor_schema(message: int):
    return custom_sensor_schema(
        message=message,
        unit_of_measurement=UNIT_PERCENT,
        accuracy_decimals=0,
        device_class=DEVICE_CLASS_HUMIDITY,
        state_class=STATE_CLASS_MEASUREMENT,
    )


def error_code_sensor_schema(message: int):
    return custom_sensor_schema(
        message=message,
        unit_of_measurement="",
        accuracy_decimals=0,
        icon="mdi:alert",
        entity_category="diagnostic",
    )


DEVICE_SCHEMA = cv.Schema(
    {
        cv.GenerateID(CONF_DEVICE_ID): cv.declare_id(Samsung_AC_Device),
        cv.Optional(CONF_CAPABILITIES): CAPABILITIES_SCHEMA,
        cv.Required(CONF_DEVICE_ADDRESS): cv.string,
        cv.Optional(CONF_DEVICE_ROOM_TEMPERATURE): sensor.sensor_schema(
            unit_of_measurement=UNIT_CELSIUS,
            accuracy_decimals=1,
            device_class=DEVICE_CLASS_TEMPERATURE,
            state_class=STATE_CLASS_MEASUREMENT,
        ),
        cv.Optional(CONF_DEVICE_ROOM_TEMPERATURE_OFFSET): cv.float_,
        cv.Optional(CONF_DEVICE_OUTDOOR_TEMPERATURE): sensor.sensor_schema(
            unit_of_measurement=UNIT_CELSIUS,
            accuracy_decimals=1,
            device_class=DEVICE_CLASS_TEMPERATURE,
            state_class=STATE_CLASS_MEASUREMENT,
        ),
        cv.Optional(CONF_DEVICE_INDOOR_EVA_IN_TEMPERATURE): sensor.sensor_schema(
            unit_of_measurement=UNIT_CELSIUS,
            accuracy_decimals=1,
            device_class=DEVICE_CLASS_TEMPERATURE,
            state_class=STATE_CLASS_MEASUREMENT,
        ),
        cv.Optional(CONF_DEVICE_INDOOR_EVA_OUT_TEMPERATURE): sensor.sensor_schema(
            unit_of_measurement=UNIT_CELSIUS,
            accuracy_decimals=1,
            device_class=DEVICE_CLASS_TEMPERATURE,
            state_class=STATE_CLASS_MEASUREMENT,
        ),
        cv.Optional(CONF_DEVICE_ERROR_CODE): error_code_sensor_schema(0x8235),
        cv.Optional(CONF_DEVICE_TARGET_TEMPERATURE): NUMBER_SCHEMA,
        cv.Optional(CONF_DEVICE_WATER_OUTLET_TARGET): NUMBER_SCHEMA,
        cv.Optional(CONF_DEVICE_WATER_TARGET_TEMPERATURE): NUMBER_SCHEMA,
        cv.Optional(CONF_DEVICE_POWER): switch.switch_schema(
            Samsung_AC_Switch, icon="mdi:power"
        ),
        cv.Optional(CONF_DEVICE_AUTOMATIC_CLEANING): switch.switch_schema(
            Samsung_AC_Switch, icon="mdi:broom"
        ),
        cv.Optional(CONF_DEVICE_WATER_HEATER_POWER): switch.switch_schema(
            Samsung_AC_Switch
        ),
        cv.Optional(CONF_DEVICE_MODE): SELECT_MODE_SCHEMA,
        cv.Optional(CONF_DEVICE_WATER_HEATER_MODE): SELECT_WATER_HEATER_MODE_SCHEMA,
        cv.Optional(CONF_DEVICE_CLIMATE): CLIMATE_SCHEMA,
        cv.Optional(CONF_MAP_AUTO_TO_HEAT_COOL, default=False): cv.boolean,
        cv.Optional(CONF_DEVICE_CUSTOM, default=[]): cv.ensure_list(
            CUSTOM_SENSOR_SCHEMA
        ),
        # keep CUSTOM_SENSOR_KEYS in sync with these
        cv.Optional(CONF_DEVICE_WATER_TEMPERATURE): temperature_sensor_schema(0x4237),
        cv.Optional(CONF_DEVICE_ROOM_HUMIDITY): humidity_sensor_schema(0x4038),
        cv.Optional(
            CONF_DEVICE_OUT_CONTROL_WATTMETER_ALL_UNIT_ACCUM
        ): sensor.sensor_schema(
            unit_of_measurement=UNIT_WATT,
            accuracy_decimals=1,
            device_class=DEVICE_CLASS_POWER,
            state_class=STATE_CLASS_MEASUREMENT,
            icon="mdi:flash",
        ),
        cv.Optional(
            CONF_DEVICE_OUT_CONTROL_WATTMETER_1W_1MIN_SUM
        ): sensor.sensor_schema(
            unit_of_measurement="kWh",
            accuracy_decimals=3,
            device_class=DEVICE_CLASS_ENERGY,
            state_class=STATE_CLASS_TOTAL_INCREASING,
            icon="mdi:counter",
        ).extend(
            {
                cv.Optional(
                    CONF_FILTERS, default=[{"multiply": 0.001}]
                ): sensor.validate_filters
            }
        ),
        cv.Optional(CONF_DEVICE_OUT_SENSOR_CT1): sensor.sensor_schema(
            unit_of_measurement=UNIT_AMPERE,
            accuracy_decimals=2,
            device_class=DEVICE_CLASS_CURRENT,
            state_class=STATE_CLASS_MEASUREMENT,
            icon="mdi:current-ac",
        ).extend(
            {
                cv.Optional(CONF_DEVICE_CUSTOM_MESSAGE, default=0x8217): cv.hex_int,
                cv.Optional(
                    CONF_FILTERS, default=[{"multiply": 0.1}]
                ): sensor.validate_filters,
            }
        ),
        cv.Optional(CONF_DEVICE_OUT_SENSOR_VOLTAGE): sensor.sensor_schema(
            unit_of_measurement=UNIT_VOLT,
            accuracy_decimals=1,
            device_class=DEVICE_CLASS_VOLTAGE,
            state_class=STATE_CLASS_MEASUREMENT,
            icon="mdi:flash",
        ).extend(
            {
                cv.Optional(CONF_DEVICE_CUSTOM_MESSAGE, default=0x24FC): cv.hex_int,
            }
        ),
        cv.Optional(
            CONF_DEVICE_OUT_OPERATION_ODU_MODE_TEXT
        ): text_sensor.text_sensor_schema(
            icon="mdi:fan",
            entity_category="diagnostic",
        ),
        cv.Optional(
            CONF_DEVICE_OUT_OPERATION_HEATCOOL_TEXT
        ): text_sensor.text_sensor_schema(
            icon="mdi:thermometer",
            entity_category="diagnostic",
        ),
        # EVA temperature sensors (read-only)
        cv.Optional(CONF_DEVICE_EVA_IN_TEMP): temperature_sensor_schema(0x4205),
        cv.Optional(CONF_DEVICE_EVA_OUT_TEMP): temperature_sensor_schema(0x4206),
        # DHW / Hydrobox read-only sensors
        cv.Optional(CONF_DEVICE_PHE_OUT_WATER_OUT): temperature_sensor_schema(0x4238),
        cv.Optional(CONF_DEVICE_PHE_IN_WATER_RETURN): temperature_sensor_schema(0x4236),
        cv.Optional(CONF_DEVICE_WATER_FLOW): custom_sensor_schema(
            message=0x42E9,
            unit_of_measurement="L/min",
            accuracy_decimals=1,
            icon="mdi:water-pump",
            state_class=STATE_CLASS_MEASUREMENT,
            raw_filters=[{"multiply": 0.1}],
        ),
        # DHW / Hydrobox writable selects
        cv.Optional(CONF_DEVICE_DHW_VALVE_DIRECTION): SELECT_GENERIC_SCHEMA,
        cv.Optional(CONF_DEVICE_DHW_DISINFECTION_DAY): SELECT_GENERIC_SCHEMA,
        # DHW / Hydrobox writable numbers
        cv.Optional(CONF_DEVICE_DHW_DISINFECTION_START_TIME): NUMBER_SCHEMA,
        cv.Optional(CONF_DEVICE_DHW_DISINFECTION_TARGET_TEMP): NUMBER_SCHEMA,
        cv.Optional(CONF_DEVICE_DHW_DISINFECTION_DURATION): NUMBER_SCHEMA,
        cv.Optional(CONF_DEVICE_DHW_DISINFECTION_MAX_TIME): NUMBER_SCHEMA,
        # Read-only sensors
        cv.Optional(CONF_DEVICE_WATER_LAW_TARGET_FLOW_TEMP): temperature_sensor_schema(0x427F),
        cv.Optional(CONF_DEVICE_INDOOR_POWER_CONSUMPTION): custom_sensor_schema(
            message=0x4284,
            unit_of_measurement=UNIT_WATT,
            accuracy_decimals=0,
            device_class=DEVICE_CLASS_POWER,
            state_class=STATE_CLASS_MEASUREMENT,
            icon="mdi:flash",
        ),
        cv.Optional(CONF_DEVICE_GENERATED_POWER_LAST_MINUTE): custom_sensor_schema(
            message=0x4426,
            unit_of_measurement="kWh",
            accuracy_decimals=3,
            device_class=DEVICE_CLASS_ENERGY,
            state_class=STATE_CLASS_TOTAL_INCREASING,
            icon="mdi:counter",
            raw_filters=[{"multiply": 0.001}],
        ),
        cv.Optional(CONF_DEVICE_DEFROST_STATUS): custom_sensor_schema(
            message=0x402E,
            accuracy_decimals=0,
            icon="mdi:snowflake-melt",
        ),
        cv.Optional(CONF_DEVICE_WATER_PUMP_STATUS): custom_sensor_schema(
            message=0x4089,
            accuracy_decimals=0,
            icon="mdi:water-pump",
        ),
        cv.Optional(CONF_DEVICE_BOOSTER_HEATER_STATUS): custom_sensor_schema(
            message=0x4087,
            accuracy_decimals=0,
            icon="mdi:fire",
        ),
        # Writable switch
        cv.Optional(CONF_DEVICE_SILENCE_MODE): switch.switch_schema(
            Samsung_AC_Switch, icon="mdi:volume-off"
        ),
        # Writable numbers
        cv.Optional(CONF_DEVICE_WATER_LAW_TARGET_TEMP_SHIFT): NUMBER_SCHEMA,
        # Heating water law curve / limits
        cv.Optional(CONF_DEVICE_HEATING_WATER_OUTLET_UPPER): NUMBER_SCHEMA,
        cv.Optional(CONF_DEVICE_HEATING_WATER_OUTLET_LOWER): NUMBER_SCHEMA,
        cv.Optional(CONF_DEVICE_HEATING_LOWER_OUTDOOR_TEMP): NUMBER_SCHEMA,
        cv.Optional(CONF_DEVICE_HEATING_UPPER_OUTDOOR_TEMP): NUMBER_SCHEMA,
        cv.Optional(CONF_DEVICE_HEATING_WATER_TEMP_COLD_OUTDOOR): NUMBER_SCHEMA,
        cv.Optional(CONF_DEVICE_HEATING_WATER_TEMP_WARM_OUTDOOR): NUMBER_SCHEMA,
        # Heating selects
        cv.Optional(CONF_DEVICE_HEATING_DHW_PRIORITY): SELECT_GENERIC_SCHEMA,
        cv.Optional(CONF_DEVICE_HEATING_INVERTER_PUMP_APPLICATION): SELECT_GENERIC_SCHEMA,
        # Heating inverter pump target delta
        cv.Optional(CONF_DEVICE_HEATING_INVERTER_PUMP_TARGET_DELTA): NUMBER_SCHEMA,
        # DHW tank temp limits
        cv.Optional(CONF_DEVICE_DHW_TANK_TEMP_UPPER): NUMBER_SCHEMA,
        cv.Optional(CONF_DEVICE_DHW_TANK_TEMP_LOWER): NUMBER_SCHEMA,
        # DHW operation mode / booster / disinfection enable / forced operation
        cv.Optional(CONF_DEVICE_DHW_OPERATION_MODE): SELECT_GENERIC_SCHEMA,
        cv.Optional(CONF_DEVICE_DHW_BOOSTER_HEATER): switch.switch_schema(
            Samsung_AC_Switch, icon="mdi:fire"
        ),
        cv.Optional(CONF_DEVICE_DHW_BOOSTER_HEATER_DELAY): NUMBER_SCHEMA,
        cv.Optional(CONF_DEVICE_DHW_BOOSTER_HEATER_OVERSHOOT): NUMBER_SCHEMA,
        cv.Optional(CONF_DEVICE_DHW_DISINFECTION_ENABLE): switch.switch_schema(
            Samsung_AC_Switch, icon="mdi:bacteria"
        ),
        cv.Optional(CONF_DEVICE_DHW_FORCED_OPERATION_TIMER): SELECT_GENERIC_SCHEMA,
        cv.Optional(CONF_DEVICE_DHW_FORCED_OPERATION_TIME): NUMBER_SCHEMA,
        # HP settings
        cv.Optional(CONF_DEVICE_HP_MAX_TEMP_ALONE): NUMBER_SCHEMA,
        cv.Optional(CONF_DEVICE_HP_TEMP_DIFF_OFF): NUMBER_SCHEMA,
        cv.Optional(CONF_DEVICE_HP_TEMP_DIFF_ON): NUMBER_SCHEMA,
        # Heating priority changeover / DHW OFF outdoor temp
        cv.Optional(CONF_DEVICE_HEATING_PRIORITY_CHANGEOVER_TEMP): NUMBER_SCHEMA,
        cv.Optional(CONF_DEVICE_HEATING_DHW_OFF_OUTDOOR_TEMP): NUMBER_SCHEMA,
    }
)

CUSTOM_SENSOR_KEYS = [
    CONF_DEVICE_WATER_TEMPERATURE,
    CONF_DEVICE_ROOM_HUMIDITY,
    CONF_DEVICE_EVA_IN_TEMP,
    CONF_DEVICE_EVA_OUT_TEMP,
    CONF_DEVICE_PHE_OUT_WATER_OUT,
    CONF_DEVICE_PHE_IN_WATER_RETURN,
    CONF_DEVICE_WATER_FLOW,
    CONF_DEVICE_WATER_LAW_TARGET_FLOW_TEMP,
    CONF_DEVICE_INDOOR_POWER_CONSUMPTION,
    CONF_DEVICE_GENERATED_POWER_LAST_MINUTE,
    CONF_DEVICE_DEFROST_STATUS,
    CONF_DEVICE_WATER_PUMP_STATUS,
    CONF_DEVICE_BOOSTER_HEATER_STATUS,
]

CONF_DEVICES = "devices"

CONF_DEBUG_MQTT_HOST = "debug_mqtt_host"
CONF_DEBUG_MQTT_PORT = "debug_mqtt_port"
CONF_DEBUG_MQTT_USERNAME = "debug_mqtt_username"
CONF_DEBUG_MQTT_PASSWORD = "debug_mqtt_password"

CONF_DEBUG_LOG_MESSAGES = "debug_log_messages"
CONF_DEBUG_LOG_MESSAGES_RAW = "debug_log_messages_raw"

CONF_NON_NASA_KEEPALIVE = "non_nasa_keepalive"

CONF_DEBUG_LOG_UNDEFINED_MESSAGES = "debug_log_undefined_messages"


CONFIG_SCHEMA = (
    cv.Schema(
        {
            cv.GenerateID(): cv.declare_id(Samsung_AC),
            # cv.Optional(CONF_PAUSE, default=False): cv.boolean,
            cv.Optional(CONF_FLOW_CONTROL_PIN): pins.gpio_output_pin_schema,
            cv.Optional(CONF_DEBUG_MQTT_HOST, default=""): cv.string,
            cv.Optional(CONF_DEBUG_MQTT_PORT, default=1883): cv.int_,
            cv.Optional(CONF_DEBUG_MQTT_USERNAME, default=""): cv.string,
            cv.Optional(CONF_DEBUG_MQTT_PASSWORD, default=""): cv.string,
            cv.Optional(CONF_DEBUG_LOG_MESSAGES, default=False): cv.boolean,
            cv.Optional(CONF_DEBUG_LOG_MESSAGES_RAW, default=False): cv.boolean,
            cv.Optional(CONF_NON_NASA_KEEPALIVE, default=False): cv.boolean,
            cv.Optional(CONF_NON_NASA_TX_DELAY_MS, default=0): cv.int_range(
                min=0, max=1000
            ),
            cv.Optional(CONF_DEBUG_LOG_UNDEFINED_MESSAGES, default=False): cv.boolean,
            cv.Optional(CONF_CAPABILITIES): CAPABILITIES_SCHEMA,
            cv.Optional(CONF_DEBUG_LOG_MESSAGES_ON_CHANGE, default=False): cv.boolean,
            cv.Required(CONF_DEVICES): cv.ensure_list(DEVICE_SCHEMA),
        }
    )
    .extend(uart.UART_DEVICE_SCHEMA)
    .extend(cv.polling_component_schema("30s"))
)


async def to_code(config):
    # For Debug_MQTT
    if CORE.is_esp8266 or CORE.is_libretiny:
        cg.add_library("heman/AsyncMqttClient-esphome", "2.0.0")

    var = cg.new_Pvariable(config[CONF_ID])
    if CONF_FLOW_CONTROL_PIN in config:
        pin = await gpio_pin_expression(config[CONF_FLOW_CONTROL_PIN])
        cg.add(var.set_flow_control_pin(pin))

    for device_index, device in enumerate(config[CONF_DEVICES]):
        var_dev = cg.new_Pvariable(
            device[CONF_DEVICE_ID], device[CONF_DEVICE_ADDRESS], var
        )

        # setup capabilities
        capabilities = device.get(CONF_CAPABILITIES, config.get(CONF_CAPABILITIES, {}))

        cg.add(
            var_dev.set_supports_fan_modes(
                capabilities.get(CONF_CAPABILITIES_FAN_MODES, True)
            )
        )

        if CONF_CAPABILITIES_VERTICAL_SWING in capabilities:
            cg.add(
                var_dev.set_supports_vertical_swing(
                    capabilities[CONF_CAPABILITIES_VERTICAL_SWING]
                )
            )

        if CONF_CAPABILITIES_HORIZONTAL_SWING in capabilities:
            cg.add(
                var_dev.set_supports_horizontal_swing(
                    capabilities[CONF_CAPABILITIES_HORIZONTAL_SWING]
                )
            )

        none_added = False
        presets = capabilities.get(CONF_PRESETS, {})

        for preset, preset_info in PRESETS.items():
            preset_conf = presets.get(preset, None)

            if isinstance(preset_conf, bool) and preset_conf:
                if not none_added:
                    none_added = True
                    cg.add(var_dev.add_alt_mode("None", 0))

                cg.add(
                    var_dev.add_alt_mode(
                        preset_info["displayName"], preset_info["value"]
                    )
                )
            elif isinstance(preset_conf, dict) and preset_conf.get(
                CONF_PRESET_ENABLED, False
            ):
                if not none_added:
                    none_added = True
                    cg.add(var_dev.add_alt_mode("None", 0))

                cg.add(
                    var_dev.add_alt_mode(
                        preset_conf.get(CONF_PRESET_NAME, preset_info["displayName"]),
                        preset_conf.get(CONF_PRESET_VALUE, preset_info["value"]),
                    )
                )

        #        if CONF_CAPABILITIES in device and CONF_ALT_MODES in device[CONF_CAPABILITIES]:
        #            cg.add(var_dev.add_alt_mode("None", 0))
        #            for alt in device[CONF_CAPABILITIES][CONF_ALT_MODES]:
        #                cg.add(var_dev.add_alt_mode(alt[CONF_ALT_MODE_NAME], alt[CONF_ALT_MODE_VALUE]))
        #        elif CONF_CAPABILITIES in config and CONF_ALT_MODES in config[CONF_CAPABILITIES]:
        #            cg.add(var_dev.add_alt_mode("None", 0))
        #            for alt in config[CONF_CAPABILITIES][CONF_ALT_MODES]:
        #                cg.add(var_dev.add_alt_mode(alt[CONF_ALT_MODE_NAME], alt[CONF_ALT_MODE_VALUE]))

        # Mapping of config keys to their corresponding methods and types
        device_actions = {
            CONF_DEVICE_POWER: (switch.new_switch, var_dev.set_power_switch),
            CONF_DEVICE_AUTOMATIC_CLEANING: (
                switch.new_switch,
                var_dev.set_automatic_cleaning_switch,
            ),
            CONF_DEVICE_WATER_HEATER_POWER: (
                switch.new_switch,
                var_dev.set_water_heater_power_switch,
            ),
            CONF_DEVICE_SILENCE_MODE: (
                switch.new_switch,
                var_dev.set_silence_mode_switch,
            ),
            CONF_DEVICE_DHW_BOOSTER_HEATER: (
                switch.new_switch,
                var_dev.set_dhw_booster_heater_switch,
            ),
            CONF_DEVICE_DHW_DISINFECTION_ENABLE: (
                switch.new_switch,
                var_dev.set_dhw_disinfection_enable_switch,
            ),
            CONF_DEVICE_ROOM_TEMPERATURE: (
                sensor.new_sensor,
                var_dev.set_room_temperature_sensor,
            ),
            CONF_DEVICE_OUTDOOR_TEMPERATURE: (
                sensor.new_sensor,
                var_dev.set_outdoor_temperature_sensor,
            ),
            CONF_DEVICE_INDOOR_EVA_IN_TEMPERATURE: (
                sensor.new_sensor,
                var_dev.set_indoor_eva_in_temperature_sensor,
            ),
            CONF_DEVICE_INDOOR_EVA_OUT_TEMPERATURE: (
                sensor.new_sensor,
                var_dev.set_indoor_eva_out_temperature_sensor,
            ),
            CONF_DEVICE_ERROR_CODE: (sensor.new_sensor, var_dev.set_error_code_sensor),
            CONF_DEVICE_OUT_CONTROL_WATTMETER_ALL_UNIT_ACCUM: (
                sensor.new_sensor,
                var_dev.set_outdoor_instantaneous_power_sensor,
            ),
            CONF_DEVICE_OUT_CONTROL_WATTMETER_1W_1MIN_SUM: (
                sensor.new_sensor,
                var_dev.set_outdoor_cumulative_energy_sensor,
            ),
            CONF_DEVICE_OUT_SENSOR_CT1: (
                sensor.new_sensor,
                var_dev.set_outdoor_current_sensor,
            ),
            CONF_DEVICE_OUT_SENSOR_VOLTAGE: (
                sensor.new_sensor,
                var_dev.set_outdoor_voltage_sensor,
            ),
            CONF_DEVICE_OUT_OPERATION_ODU_MODE_TEXT: (
                text_sensor.new_text_sensor,
                var_dev.set_outdoor_operation_odu_mode_text_sensor,
            ),
            CONF_DEVICE_OUT_OPERATION_HEATCOOL_TEXT: (
                text_sensor.new_text_sensor,
                var_dev.set_outdoor_operation_heatcool_text_sensor,
            ),
        }

        # Iterate over the actions
        for key, (action, method) in device_actions.items():
            if key in device:
                conf = device[key]
                sens = await action(conf)
                cg.add(method(sens))

        if CONF_DEVICE_ROOM_TEMPERATURE_OFFSET in device:
            cg.add(
                var_dev.set_room_temperature_offset(
                    device[CONF_DEVICE_ROOM_TEMPERATURE_OFFSET]
                )
            )

        if CONF_DEVICE_WATER_TARGET_TEMPERATURE in device:
            conf = device[CONF_DEVICE_WATER_TARGET_TEMPERATURE]
            conf[CONF_UNIT_OF_MEASUREMENT] = UNIT_CELSIUS
            conf[CONF_DEVICE_CLASS] = DEVICE_CLASS_TEMPERATURE
            num = await number.new_number(
                conf, min_value=30.0, max_value=70.0, step=0.5
            )
            cg.add(var_dev.set_target_water_temperature_number(num))

        if CONF_DEVICE_TARGET_TEMPERATURE in device:
            conf = device[CONF_DEVICE_TARGET_TEMPERATURE]
            conf[CONF_UNIT_OF_MEASUREMENT] = UNIT_CELSIUS
            conf[CONF_DEVICE_CLASS] = DEVICE_CLASS_TEMPERATURE
            num = await number.new_number(
                conf, min_value=16.0, max_value=30.0, step=1.0
            )
            cg.add(var_dev.set_target_temperature_number(num))

        if CONF_DEVICE_WATER_OUTLET_TARGET in device:
            conf = device[CONF_DEVICE_WATER_OUTLET_TARGET]
            conf[CONF_UNIT_OF_MEASUREMENT] = UNIT_CELSIUS
            conf[CONF_DEVICE_CLASS] = DEVICE_CLASS_TEMPERATURE
            num = await number.new_number(
                conf, min_value=15.0, max_value=55.0, step=0.1
            )
            cg.add(var_dev.set_water_outlet_target_number(num))

        if CONF_DEVICE_MODE in device:
            conf = device[CONF_DEVICE_MODE]
            values = ["Auto", "Cool", "Dry", "Fan", "Heat"]
            sel = await select.new_select(conf, options=values)
            cg.add(var_dev.set_mode_select(sel))

        if CONF_DEVICE_WATER_HEATER_MODE in device:
            conf = device[CONF_DEVICE_WATER_HEATER_MODE]
            values = ["Eco", "Standard", "Power", "Force"]
            sel = await select.new_select(conf, options=values)
            cg.add(var_dev.set_water_heater_mode_select(sel))

        if CONF_DEVICE_DHW_VALVE_DIRECTION in device:
            conf = device[CONF_DEVICE_DHW_VALVE_DIRECTION]
            values = ["Room", "Tank"]
            sel = await select.new_select(conf, options=values)
            cg.add(var_dev.set_dhw_valve_direction_select(sel))

        if CONF_DEVICE_DHW_DISINFECTION_DAY in device:
            conf = device[CONF_DEVICE_DHW_DISINFECTION_DAY]
            values = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Everyday"]
            sel = await select.new_select(conf, options=values)
            cg.add(var_dev.set_dhw_disinfection_day_select(sel))

        if CONF_DEVICE_DHW_DISINFECTION_START_TIME in device:
            conf = device[CONF_DEVICE_DHW_DISINFECTION_START_TIME]
            num = await number.new_number(
                conf, min_value=0, max_value=23, step=1
            )
            cg.add(var_dev.set_dhw_disinfection_start_time_number(num))

        if CONF_DEVICE_DHW_DISINFECTION_TARGET_TEMP in device:
            conf = device[CONF_DEVICE_DHW_DISINFECTION_TARGET_TEMP]
            conf[CONF_UNIT_OF_MEASUREMENT] = UNIT_CELSIUS
            conf[CONF_DEVICE_CLASS] = DEVICE_CLASS_TEMPERATURE
            num = await number.new_number(
                conf, min_value=40.0, max_value=70.0, step=5.0
            )
            cg.add(var_dev.set_dhw_disinfection_target_temp_number(num))

        if CONF_DEVICE_DHW_DISINFECTION_DURATION in device:
            conf = device[CONF_DEVICE_DHW_DISINFECTION_DURATION]
            num = await number.new_number(
                conf, min_value=5, max_value=60, step=5
            )
            cg.add(var_dev.set_dhw_disinfection_duration_number(num))

        if CONF_DEVICE_DHW_DISINFECTION_MAX_TIME in device:
            conf = device[CONF_DEVICE_DHW_DISINFECTION_MAX_TIME]
            num = await number.new_number(
                conf, min_value=60, max_value=1440, step=60
            )
            cg.add(var_dev.set_dhw_disinfection_max_time_number(num))

        if CONF_DEVICE_WATER_LAW_TARGET_TEMP_SHIFT in device:
            conf = device[CONF_DEVICE_WATER_LAW_TARGET_TEMP_SHIFT]
            conf[CONF_UNIT_OF_MEASUREMENT] = UNIT_CELSIUS
            conf[CONF_DEVICE_CLASS] = DEVICE_CLASS_TEMPERATURE
            num = await number.new_number(
                conf, min_value=-5.0, max_value=5.0, step=0.5
            )
            cg.add(var_dev.set_water_law_target_temp_shift_number(num))

        if CONF_DEVICE_HEATING_WATER_OUTLET_UPPER in device:
            conf = device[CONF_DEVICE_HEATING_WATER_OUTLET_UPPER]
            conf[CONF_UNIT_OF_MEASUREMENT] = UNIT_CELSIUS
            conf[CONF_DEVICE_CLASS] = DEVICE_CLASS_TEMPERATURE
            num = await number.new_number(
                conf, min_value=37.0, max_value=70.0, step=1.0
            )
            cg.add(var_dev.set_heating_water_outlet_upper_number(num))

        if CONF_DEVICE_HEATING_WATER_OUTLET_LOWER in device:
            conf = device[CONF_DEVICE_HEATING_WATER_OUTLET_LOWER]
            conf[CONF_UNIT_OF_MEASUREMENT] = UNIT_CELSIUS
            conf[CONF_DEVICE_CLASS] = DEVICE_CLASS_TEMPERATURE
            num = await number.new_number(
                conf, min_value=15.0, max_value=37.0, step=1.0
            )
            cg.add(var_dev.set_heating_water_outlet_lower_number(num))

        if CONF_DEVICE_HEATING_LOWER_OUTDOOR_TEMP in device:
            conf = device[CONF_DEVICE_HEATING_LOWER_OUTDOOR_TEMP]
            conf[CONF_UNIT_OF_MEASUREMENT] = UNIT_CELSIUS
            conf[CONF_DEVICE_CLASS] = DEVICE_CLASS_TEMPERATURE
            num = await number.new_number(
                conf, min_value=-20.0, max_value=5.0, step=1.0
            )
            cg.add(var_dev.set_heating_lower_outdoor_temp_number(num))

        if CONF_DEVICE_HEATING_UPPER_OUTDOOR_TEMP in device:
            conf = device[CONF_DEVICE_HEATING_UPPER_OUTDOOR_TEMP]
            conf[CONF_UNIT_OF_MEASUREMENT] = UNIT_CELSIUS
            conf[CONF_DEVICE_CLASS] = DEVICE_CLASS_TEMPERATURE
            num = await number.new_number(
                conf, min_value=10.0, max_value=20.0, step=1.0
            )
            cg.add(var_dev.set_heating_upper_outdoor_temp_number(num))

        if CONF_DEVICE_HEATING_WATER_TEMP_COLD_OUTDOOR in device:
            conf = device[CONF_DEVICE_HEATING_WATER_TEMP_COLD_OUTDOOR]
            conf[CONF_UNIT_OF_MEASUREMENT] = UNIT_CELSIUS
            conf[CONF_DEVICE_CLASS] = DEVICE_CLASS_TEMPERATURE
            num = await number.new_number(
                conf, min_value=17.0, max_value=65.0, step=1.0
            )
            cg.add(var_dev.set_heating_water_temp_cold_outdoor_number(num))

        if CONF_DEVICE_HEATING_WATER_TEMP_WARM_OUTDOOR in device:
            conf = device[CONF_DEVICE_HEATING_WATER_TEMP_WARM_OUTDOOR]
            conf[CONF_UNIT_OF_MEASUREMENT] = UNIT_CELSIUS
            conf[CONF_DEVICE_CLASS] = DEVICE_CLASS_TEMPERATURE
            num = await number.new_number(
                conf, min_value=17.0, max_value=65.0, step=1.0
            )
            cg.add(var_dev.set_heating_water_temp_warm_outdoor_number(num))

        if CONF_DEVICE_HEATING_DHW_PRIORITY in device:
            conf = device[CONF_DEVICE_HEATING_DHW_PRIORITY]
            values = ["DHW", "Heating"]
            sel = await select.new_select(conf, options=values)
            cg.add(var_dev.set_heating_dhw_priority_select(sel))

        if CONF_DEVICE_HEATING_INVERTER_PUMP_APPLICATION in device:
            conf = device[CONF_DEVICE_HEATING_INVERTER_PUMP_APPLICATION]
            values = ["No", "100%", "70%"]
            sel = await select.new_select(conf, options=values)
            cg.add(var_dev.set_heating_inverter_pump_application_select(sel))

        if CONF_DEVICE_HEATING_INVERTER_PUMP_TARGET_DELTA in device:
            conf = device[CONF_DEVICE_HEATING_INVERTER_PUMP_TARGET_DELTA]
            conf[CONF_UNIT_OF_MEASUREMENT] = UNIT_CELSIUS
            conf[CONF_DEVICE_CLASS] = DEVICE_CLASS_TEMPERATURE
            num = await number.new_number(
                conf, min_value=2.0, max_value=8.0, step=1.0
            )
            cg.add(var_dev.set_heating_inverter_pump_target_delta_number(num))

        if CONF_DEVICE_DHW_TANK_TEMP_UPPER in device:
            conf = device[CONF_DEVICE_DHW_TANK_TEMP_UPPER]
            conf[CONF_UNIT_OF_MEASUREMENT] = UNIT_CELSIUS
            conf[CONF_DEVICE_CLASS] = DEVICE_CLASS_TEMPERATURE
            num = await number.new_number(
                conf, min_value=50.0, max_value=70.0, step=1.0
            )
            cg.add(var_dev.set_dhw_tank_temp_upper_number(num))

        if CONF_DEVICE_DHW_TANK_TEMP_LOWER in device:
            conf = device[CONF_DEVICE_DHW_TANK_TEMP_LOWER]
            conf[CONF_UNIT_OF_MEASUREMENT] = UNIT_CELSIUS
            conf[CONF_DEVICE_CLASS] = DEVICE_CLASS_TEMPERATURE
            num = await number.new_number(
                conf, min_value=30.0, max_value=40.0, step=1.0
            )
            cg.add(var_dev.set_dhw_tank_temp_lower_number(num))

        if CONF_DEVICE_DHW_OPERATION_MODE in device:
            conf = device[CONF_DEVICE_DHW_OPERATION_MODE]
            values = ["Off", "Thermo ON/OFF", "On demand"]
            sel = await select.new_select(conf, options=values)
            cg.add(var_dev.set_dhw_operation_mode_select(sel))

        if CONF_DEVICE_HP_MAX_TEMP_ALONE in device:
            conf = device[CONF_DEVICE_HP_MAX_TEMP_ALONE]
            conf[CONF_UNIT_OF_MEASUREMENT] = UNIT_CELSIUS
            conf[CONF_DEVICE_CLASS] = DEVICE_CLASS_TEMPERATURE
            num = await number.new_number(
                conf, min_value=45.0, max_value=55.0, step=1.0
            )
            cg.add(var_dev.set_hp_max_temp_alone_number(num))

        if CONF_DEVICE_HP_TEMP_DIFF_OFF in device:
            conf = device[CONF_DEVICE_HP_TEMP_DIFF_OFF]
            conf[CONF_UNIT_OF_MEASUREMENT] = UNIT_CELSIUS
            conf[CONF_DEVICE_CLASS] = DEVICE_CLASS_TEMPERATURE
            num = await number.new_number(
                conf, min_value=0.0, max_value=10.0, step=1.0
            )
            cg.add(var_dev.set_hp_temp_diff_off_number(num))

        if CONF_DEVICE_HP_TEMP_DIFF_ON in device:
            conf = device[CONF_DEVICE_HP_TEMP_DIFF_ON]
            conf[CONF_UNIT_OF_MEASUREMENT] = UNIT_CELSIUS
            conf[CONF_DEVICE_CLASS] = DEVICE_CLASS_TEMPERATURE
            num = await number.new_number(
                conf, min_value=5.0, max_value=30.0, step=1.0
            )
            cg.add(var_dev.set_hp_temp_diff_on_number(num))

        if CONF_DEVICE_DHW_BOOSTER_HEATER_DELAY in device:
            conf = device[CONF_DEVICE_DHW_BOOSTER_HEATER_DELAY]
            num = await number.new_number(
                conf, min_value=20, max_value=95, step=5
            )
            cg.add(var_dev.set_dhw_booster_heater_delay_number(num))

        if CONF_DEVICE_DHW_BOOSTER_HEATER_OVERSHOOT in device:
            conf = device[CONF_DEVICE_DHW_BOOSTER_HEATER_OVERSHOOT]
            conf[CONF_UNIT_OF_MEASUREMENT] = UNIT_CELSIUS
            conf[CONF_DEVICE_CLASS] = DEVICE_CLASS_TEMPERATURE
            num = await number.new_number(
                conf, min_value=0.0, max_value=4.0, step=1.0
            )
            cg.add(var_dev.set_dhw_booster_heater_overshoot_number(num))

        if CONF_DEVICE_DHW_FORCED_OPERATION_TIMER in device:
            conf = device[CONF_DEVICE_DHW_FORCED_OPERATION_TIMER]
            values = ["No timer", "Timer"]
            sel = await select.new_select(conf, options=values)
            cg.add(var_dev.set_dhw_forced_operation_timer_select(sel))

        if CONF_DEVICE_DHW_FORCED_OPERATION_TIME in device:
            conf = device[CONF_DEVICE_DHW_FORCED_OPERATION_TIME]
            num = await number.new_number(
                conf, min_value=3, max_value=30, step=1
            )
            cg.add(var_dev.set_dhw_forced_operation_time_number(num))

        if CONF_DEVICE_HEATING_PRIORITY_CHANGEOVER_TEMP in device:
            conf = device[CONF_DEVICE_HEATING_PRIORITY_CHANGEOVER_TEMP]
            conf[CONF_UNIT_OF_MEASUREMENT] = UNIT_CELSIUS
            conf[CONF_DEVICE_CLASS] = DEVICE_CLASS_TEMPERATURE
            num = await number.new_number(
                conf, min_value=-15.0, max_value=20.0, step=1.0
            )
            cg.add(var_dev.set_heating_priority_changeover_temp_number(num))

        if CONF_DEVICE_HEATING_DHW_OFF_OUTDOOR_TEMP in device:
            conf = device[CONF_DEVICE_HEATING_DHW_OFF_OUTDOOR_TEMP]
            conf[CONF_UNIT_OF_MEASUREMENT] = UNIT_CELSIUS
            conf[CONF_DEVICE_CLASS] = DEVICE_CLASS_TEMPERATURE
            num = await number.new_number(
                conf, min_value=14.0, max_value=35.0, step=1.0
            )
            cg.add(var_dev.set_heating_dhw_off_outdoor_temp_number(num))

        if CONF_DEVICE_CLIMATE in device:
            conf = device[CONF_DEVICE_CLIMATE]
            var_cli = cg.new_Pvariable(conf[CONF_ID])
            await climate.register_climate(var_cli, conf)
            cg.add(var_dev.set_climate(var_cli))

            # Optional UI mapping: expose Samsung Auto as HA Heat/Cool
            cg.add(
                var_dev.set_map_auto_to_heat_cool(
                    device.get(CONF_MAP_AUTO_TO_HEAT_COOL, False)
                )
            )

        if CONF_DEVICE_CUSTOM in device:
            for cust_sens in device[CONF_DEVICE_CUSTOM]:
                sens = await sensor.new_sensor(cust_sens)
                cg.add(
                    var_dev.add_custom_sensor(
                        cust_sens[CONF_DEVICE_CUSTOM_MESSAGE], sens
                    )
                )

        for key in CUSTOM_SENSOR_KEYS:
            if key in device:
                conf = device[key]
                # combine raw filters with any user-defined filters
                conf_copy = conf.copy()
                conf_copy[CONF_FILTERS] = (
                    conf[CONF_DEVICE_CUSTOM_RAW_FILTERS]
                    if CONF_DEVICE_CUSTOM_RAW_FILTERS in conf
                    else []
                ) + (conf[CONF_FILTERS] if CONF_FILTERS in conf else [])
                sens = await sensor.new_sensor(conf_copy)
                cg.add(
                    var_dev.add_custom_sensor(conf[CONF_DEVICE_CUSTOM_MESSAGE], sens)
                )

        cg.add(var.register_device(var_dev))

    # If debug MQTT is enabled on ESP32, we need ESP-IDF's built-in mqtt component.
    # ESPHome may exclude it by default to reduce compile time, so re-enable it only when needed.
    if CORE.is_esp32 and config[CONF_DEBUG_MQTT_HOST]:
        cg.add_define("SAMSUNG_AC_DEBUG_MQTT")
        try:
            from esphome.components.esp32 import include_builtin_idf_component

            include_builtin_idf_component("mqtt")
        except Exception:
            try:
                from esphome.components.esp32 import include_idf_component

                include_idf_component("mqtt")
            except Exception:
                from esphome.components.esp32 import add_idf_component

                add_idf_component("mqtt")

    cg.add(
        var.set_debug_mqtt(
            config[CONF_DEBUG_MQTT_HOST],
            config[CONF_DEBUG_MQTT_PORT],
            config[CONF_DEBUG_MQTT_USERNAME],
            config[CONF_DEBUG_MQTT_PASSWORD],
        )
    )

    # Mapping of config keys to their corresponding methods
    config_actions = {
        CONF_DEBUG_LOG_MESSAGES: var.set_debug_log_messages,
        CONF_DEBUG_LOG_MESSAGES_RAW: var.set_debug_log_messages_raw,
        CONF_NON_NASA_KEEPALIVE: var.set_non_nasa_keepalive,
        CONF_NON_NASA_TX_DELAY_MS: var.set_non_nasa_tx_delay_ms,
        CONF_DEBUG_LOG_UNDEFINED_MESSAGES: var.set_debug_log_undefined_messages,
        CONF_DEBUG_LOG_MESSAGES_ON_CHANGE: var.set_debug_log_messages_on_change,
    }

    # Iterate over the actions
    for key, method in config_actions.items():
        if key in config:
            cg.add(method(config[key]))

    await cg.register_component(var, config)
    await uart.register_uart_device(var, config)
