#pragma once

#include <set>
#include "esphome/core/optional.h"
#include "util.h"

namespace esphome
{
    namespace samsung_ac
    {
        extern bool non_nasa_keepalive;
        extern uint16_t non_nasa_tx_delay_ms;

        enum class DecodeResultType
        {
            Fill = 1,
            Discard = 2,
            Processed = 3
        };

        struct DecodeResult
        {
            DecodeResultType type;
            uint16_t bytes; // when Processed
        };

        enum class Mode
        {
            Unknown = -1,
            Auto = 0,
            Cool = 1,
            Dry = 2,
            Fan = 3,
            Heat = 4,
        };

        enum class WaterHeaterMode
        {
            Unknown = -1,
            Eco = 0,
            Standard = 1,
            Power = 2,
            Force = 3,
        };

        enum class FanMode
        {
            Unknown = -1,
            Auto = 0,
            Low = 1,
            Mid = 2,
            High = 3,
            Turbo = 4,
            Off = 5
        };

        typedef std::string AltModeName;
        typedef uint8_t AltMode;

        struct AltModeDesc
        {
            AltModeName name;
            AltMode value;
        };

        enum class SwingMode : uint8_t
        {
            Fix = 0,
            Vertical = 1,
            Horizontal = 2,
            All = 3
        };

        class MessageTarget
        {
        public:
            virtual uint32_t get_miliseconds() = 0;
            virtual void publish_data(uint8_t id, std::vector<uint8_t> &&data) = 0;
            virtual void ack_data(uint8_t id) = 0;
            virtual void register_address(const std::string address) = 0;
            virtual void set_power(const std::string address, bool value) = 0;
            virtual void set_automatic_cleaning(const std::string address, bool value) = 0;
            virtual void set_water_heater_power(const std::string address, bool value) = 0;
            virtual void set_room_temperature(const std::string address, float value) = 0;
            virtual void set_target_temperature(const std::string address, float value) = 0;
            virtual void set_water_outlet_target(const std::string address, float value) = 0;
            virtual void set_outdoor_temperature(const std::string address, float value) = 0;
            virtual void set_indoor_eva_in_temperature(const std::string address, float value) = 0;
            virtual void set_indoor_eva_out_temperature(const std::string address, float value) = 0;
            virtual void set_target_water_temperature(const std::string address, float value) = 0;
            virtual void set_mode(const std::string address, Mode mode) = 0;
            virtual void set_water_heater_mode(const std::string address, WaterHeaterMode waterheatermode) = 0;
            virtual void set_fanmode(const std::string address, FanMode fanmode) = 0;
            virtual void set_altmode(const std::string address, AltMode altmode) = 0;
            virtual void set_swing_vertical(const std::string address, bool vertical) = 0;
            virtual void set_swing_horizontal(const std::string address, bool horizontal) = 0;
            virtual void set_custom_sensor(const std::string address, uint16_t message_number, float value) = 0;
            virtual void set_error_code(const std::string address, int error_code) = 0;
            virtual void set_outdoor_instantaneous_power(const std::string &address, float value) = 0;
            virtual void set_outdoor_cumulative_energy(const std::string &address, float value) = 0;
            virtual void set_outdoor_current(const std::string &address, float value) = 0;
            virtual void set_outdoor_voltage(const std::string &address, float value) = 0;
            virtual void set_outdoor_operation_odu_mode_text_sensor(const std::string &address, int value) = 0;
            virtual void set_outdoor_operation_heatcool_text_sensor(const std::string &address, int value) = 0;
            virtual void set_dhw_valve_direction(const std::string address, int value) = 0;
            virtual void set_dhw_disinfection_day(const std::string address, int value) = 0;
            virtual void set_dhw_disinfection_start_time(const std::string address, int value) = 0;
            virtual void set_dhw_disinfection_target_temp(const std::string address, float value) = 0;
            virtual void set_dhw_disinfection_duration(const std::string address, int value) = 0;
            virtual void set_dhw_disinfection_max_time(const std::string address, int value) = 0;
            virtual void set_silence_mode(const std::string address, bool value) = 0;
            virtual void set_water_law_target_temp_shift(const std::string address, float value) = 0;
            virtual void set_heating_water_outlet_upper(const std::string address, float value) = 0;
            virtual void set_heating_water_outlet_lower(const std::string address, float value) = 0;
            virtual void set_heating_lower_outdoor_temp(const std::string address, float value) = 0;
            virtual void set_heating_upper_outdoor_temp(const std::string address, float value) = 0;
            virtual void set_heating_water_temp_cold_outdoor(const std::string address, float value) = 0;
            virtual void set_heating_water_temp_warm_outdoor(const std::string address, float value) = 0;
            virtual void set_heating_dhw_priority(const std::string address, int value) = 0;
            virtual void set_heating_inverter_pump_application(const std::string address, int value) = 0;
            virtual void set_heating_inverter_pump_target_delta(const std::string address, float value) = 0;
            virtual void set_dhw_tank_temp_upper(const std::string address, float value) = 0;
            virtual void set_dhw_tank_temp_lower(const std::string address, float value) = 0;
            virtual void set_dhw_operation_mode(const std::string address, int value) = 0;
            virtual void set_hp_max_temp_alone(const std::string address, float value) = 0;
            virtual void set_hp_temp_diff_off(const std::string address, float value) = 0;
            virtual void set_hp_temp_diff_on(const std::string address, float value) = 0;
            virtual void set_dhw_booster_heater(const std::string address, bool value) = 0;
            virtual void set_dhw_booster_heater_delay(const std::string address, int value) = 0;
            virtual void set_dhw_booster_heater_overshoot(const std::string address, float value) = 0;
            virtual void set_dhw_disinfection_enable(const std::string address, bool value) = 0;
            virtual void set_dhw_forced_operation_timer(const std::string address, int value) = 0;
            virtual void set_dhw_forced_operation_time(const std::string address, int value) = 0;
            virtual void set_heating_priority_changeover_temp(const std::string address, float value) = 0;
            virtual void set_heating_dhw_off_outdoor_temp(const std::string address, float value) = 0;
        };

        struct ProtocolRequest
        {
        public:
            optional<bool> power;
            optional<bool> automatic_cleaning;
            optional<bool> water_heater_power;
            optional<Mode> mode;
            optional<WaterHeaterMode> waterheatermode;
            optional<float> target_temp;
            optional<float> water_outlet_target;
            optional<float> target_water_temp;
            optional<FanMode> fan_mode;
            optional<SwingMode> swing_mode;
            optional<AltMode> alt_mode;
            optional<int> dhw_valve_direction;
            optional<int> dhw_disinfection_day;
            optional<int> dhw_disinfection_start_time;
            optional<float> dhw_disinfection_target_temp;
            optional<int> dhw_disinfection_duration;
            optional<int> dhw_disinfection_max_time;
            optional<bool> silence_mode;
            optional<float> water_law_target_temp_shift;
            optional<float> heating_water_outlet_upper;
            optional<float> heating_water_outlet_lower;
            optional<float> heating_lower_outdoor_temp;
            optional<float> heating_upper_outdoor_temp;
            optional<float> heating_water_temp_cold_outdoor;
            optional<float> heating_water_temp_warm_outdoor;
            optional<int> heating_dhw_priority;
            optional<int> heating_inverter_pump_application;
            optional<float> heating_inverter_pump_target_delta;
            optional<float> dhw_tank_temp_upper;
            optional<float> dhw_tank_temp_lower;
            optional<int> dhw_operation_mode;
            optional<float> hp_max_temp_alone;
            optional<float> hp_temp_diff_off;
            optional<float> hp_temp_diff_on;
            optional<bool> dhw_booster_heater;
            optional<int> dhw_booster_heater_delay;
            optional<float> dhw_booster_heater_overshoot;
            optional<bool> dhw_disinfection_enable;
            optional<int> dhw_forced_operation_timer;
            optional<int> dhw_forced_operation_time;
            optional<float> heating_priority_changeover_temp;
            optional<float> heating_dhw_off_outdoor_temp;
        };

        class Protocol
        {
        public:
            virtual void publish_request(MessageTarget *target, const std::string &address, ProtocolRequest &request) = 0;
            virtual void protocol_update(MessageTarget *target) = 0;
        };

        enum class ProtocolProcessing
        {
            Auto = 0,
            NASA = 1,
            NonNASA = 2
        };

        extern ProtocolProcessing protocol_processing;

        DecodeResult process_data(std::vector<uint8_t> &data, MessageTarget *target);

        Protocol *get_protocol(const std::string &address);

        bool is_nasa_address(const std::string &address);

        enum class AddressType
        {
            Outdoor = 0,
            Indoor = 1,
            Other = 2
        };

        AddressType get_address_type(const std::string &address);

    } // namespace samsung_ac
} // namespace esphome
