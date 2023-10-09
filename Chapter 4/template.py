import time, sys
from fhict_cb_01.custom_telemetrix import CustomTelemetrix

#-----------
# Constants
#-----------

#------------------------------
# Initialized global variables
#------------------------------

#-----------
# functions
#-----------
def setup():
    global board
    board = CustomTelemetrix()
    # Put your code here.

def loop():
    # Put your code here.
    time.sleep(0.01) # Give Firmata some time to handle the protocol.

# Put your functions here.

#--------------
# main program
#--------------
setup()
while True:
    try:
        loop()
    except KeyboardInterrupt: # Shutdown Firmata on Crtl+C.
        print ('shutdown')
        board.shutdown()
        sys.exit(0)  
