import time
import sys
from fhict_cb_01.custom_telemetrix import CustomTelemetrix


# -----------
# Constants
# -----------
BUTTON1PIN = 8
REDLEDPIN = 4


# -----------
# functions
# -----------
def setup():
    global board
    board = CustomTelemetrix()
    # set pin to input pullup
    board.set_pin_mode_digital_input_pullup(BUTTON1PIN)
    board.set_pin_mode_digital_output(REDLEDPIN)


def loop():
    time.sleep(0.01)  # Give Firmata some time to handle protocol.
    data = board.digital_read(BUTTON1PIN)
    if data:
        level = data[0]
        print(level)

        if (level == 0):
            board.digital_write(REDLEDPIN, 1)
        else:
            board.digital_write(REDLEDPIN, 0)


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
