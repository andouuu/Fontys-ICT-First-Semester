import time
from fhict_cb_01.custom_telemetrix import CustomTelemetrix
board = CustomTelemetrix()

board.displayShow(8173)
time.sleep(1)

board.displayShow(-0)
time.sleep(1)

board.displayShow("1E4A")
time.sleep(1)

board.displayShow(54)
time.sleep(1)

board.displayShow(0)
time.sleep(1)

board.displayShow(-137)
time.sleep(1)

board.displayShow('-3.141f')
time.sleep(1)

board.displayShow('3.141f')
time.sleep(1)

board.displayShow('0.643f')
time.sleep(1)

board.displayShow('-0.495f')
time.sleep(1)

board.displayShow('-0.00f')
time.sleep(1)
board.displayOff()
board.shutdown()
