from fhict_cb_01.custom_telemetrix import CustomTelemetrix
import time, sys

#-----------
# Constants
#-----------
POTPIN = 0 # analog pin A0

#-----------
# functions
#-----------
def setup():
    global board
    board = CustomTelemetrix()
    board.set_pin_mode_analog_input(POTPIN)
    time.sleep(0.1)

def loop():
    value, timestamp = board.analog_read(POTPIN)
    print(value)

#--------------
# main program
#--------------
setup()
while True:
    try:
        loop()
    except KeyboardInterrupt: # crtl+C
        print ('shutdown')
        board.shutdown()
        sys.exit(0)  
