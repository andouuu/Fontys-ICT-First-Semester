import time,sys
from fhict_cb_01.custom_telemetrix import CustomTelemetrix
board = CustomTelemetrix()

BUTTON1 = 8
DHTPIN=12
LDRPIN=2
#------------------------------
# Initialized global variables
#------------------------------
level = 0
prevLevel = 0
temperature=0
humidity=0
light=0
count=-1
measuresList=[]
#-----------
# functions
#-----------
def ButtonChanged(data):
    global level
    level = data[2] # get the level
    # Keep the callback function short and fast.
    # Let loop() do the 'expensive' tasks.

def Measure(data):
    global humidity, temperature
    # [report_type, error_value, pin, dht_type, humidity, temperature, timestamp]
    if (data[1] == 0):
        humidity = data[4]
        temperature = data[5]

def LDRChanged(data):
    global light
    light = data[2]
    # print(data)

def setup():
    board.set_pin_mode_digital_input_pullup(BUTTON1, callback = ButtonChanged)
    board.set_pin_mode_dht(DHTPIN, dht_type=11, callback=Measure)
    board.set_pin_mode_analog_input(
    LDRPIN, callback=LDRChanged, differential=10)
    

def loop():
    global level
    global prevLevel
    global count
    global light
    measuresList=[temperature,humidity,light]
    if level!=prevLevel:
        if (level==0):
            # Lets respond on button level change.
            count+=1
            if count==len(measuresList):
                count-=len(measuresList)
            board.displayOn()    
            board.displayShow(measuresList[count])
        prevLevel = level    
    time.sleep(0.01)
        
    
    

#--------------
# main program
#--------------
setup()
board.displayOff()
while True:
    try:
        loop()
    except KeyboardInterrupt: # crtl+C
        print ('shutdown')
        board.shutdown()
        sys.exit(0)