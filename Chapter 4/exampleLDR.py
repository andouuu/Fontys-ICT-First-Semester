from fhict_cb_01.custom_telemetrix import CustomTelemetrix
import time

# This example demonstrates reading the light dependent resistor
# with a callback function.

board = CustomTelemetrix()

# The analog input pin that the Light Dependent Resitor (LDR)
# is attached to
LDR_PIN = 2

# Here we define a callback function


def callback_ldr(data):
    # data list contains the following:
    # [pin_type, pin_number, pin_value, raw_time_stamp]
    sensor_value = data[2]
    resistance_sensor = (1023-sensor_value)*10/sensor_value
    print(
        f"The resistance of the light sensor is: {resistance_sensor:.1f} KOhm")

    klux = 325 * pow(resistance_sensor, -1.4) / 1000
    board.displayShow(klux)
    print(f"Illuminance is approximately {klux:.3f} Kilo lux")


# We set the callback function so that any change of more than 50 units
# in the sensor results in calling the supplied function "callback_ldr"
board.set_pin_mode_analog_input(
    LDR_PIN, callback=callback_ldr, differential=50)

# infinite loop with a short (10 millisecond) pause to avoid overloading the CPU
while True:
    try:
        time.sleep(0.01)
    # if anyone presses <CTRL+C> break out of the loop
    except KeyboardInterrupt:
        break

# clean up
print("Shutting down...")
board.shutdown()
