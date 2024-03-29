
import time
import serial

from RPi_Keyboard3 import Keyboard
kbd = Keyboard()
ser = serial.Serial(

               port='/dev/ttyS0',
               baudrate = 9600,
               parity=serial.PARITY_NONE,
               stopbits=serial.STOPBITS_ONE,
               bytesize=serial.EIGHTBITS,
               timeout=.1
           )
while 1:
    inp = None
    try:
       inp = ser.readline()
       print(inp)
       time.sleep(.01)
    except Exception as e:
        print(e)
        time.sleep(.1)
        continue

    if not inp:continue

    try:
        kbd.keyout(inp.decode())
    except Exception as e:
        print(e)
        time.sleep(.1)
