from fhict_cb_01.custom_telemetrix import CustomTelemetrix
import time, sys


#-----------
# Constants
#-----------
POTPIN = 0 # analog pin A0
MAX_ANGLE = 270 # degrees
#------------------------------
# Initialized global variables
#------------------------------
value = 0

#-----------
# functions
#-----------
def PotChanged(data):
    global value
    value = data[2]

   

def setup():
    global board
    board = CustomTelemetrix()
    board.set_pin_mode_analog_input(POTPIN, callback=PotChanged, differential=10)
    # Note: The differential defines the distance between the previous 
    #       and current value. If the difference is greater dan differential 
    #       then PotChange() is called. This solution reduces noise.

def loop():
    angle = value * MAX_ANGLE/1023.0
    print(f"The angle is : {angle:.1f}")
    time.sleep(0.5)

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
