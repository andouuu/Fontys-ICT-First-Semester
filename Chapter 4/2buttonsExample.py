import time
import sys
from fhict_cb_01.custom_telemetrix import CustomTelemetrix

# -----------
# Constants
# -----------
BUTTON1PIN = 8
BUTTON2PIN = 9

# -----------
# functions
# -----------


def setup():
    global board
    board = CustomTelemetrix()
    board.set_pin_mode_digital_input_pullup(
        BUTTON1PIN)  # set pin to input pullup
    board.set_pin_mode_digital_input_pullup(
        BUTTON2PIN)  # set pin to input pullup
    # wait for board to be ready
    time.sleep(0.1)


def loop():
    level1, time_stamp1 = board.digital_read(BUTTON1PIN)
    level2, time_stamp2 = board.digital_read(BUTTON2PIN)
    print(level1, level2)

    time.sleep(0.01)  # Give Firmata some time to handle protocol.

    # value = board.digital_read(8)
    # print(value) # returns a list of level and
    # option 1:
    # level = board.digital_read(8)[0]
    # option 2:
    # level, time_stamp = board.digital_read(8)


# --------------
# main program
# --------------
setup()
while True:
    try:
        loop()
    except KeyboardInterrupt:  # crtl+C
        print('shutdown')
        board.shutdown()
        sys.exit(0)
