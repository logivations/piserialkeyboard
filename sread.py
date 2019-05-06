
import time
import serial


ser = serial.Serial(

               port='/dev/ttyS0',
               baudrate = 115200,
               parity=serial.PARITY_NONE,
               stopbits=serial.STOPBITS_ONE,
               bytesize=serial.EIGHTBITS,
               timeout=.1
           )
while 1:
    inp = None
    try:
       inp = ser.readline()
       time.sleep(.01)
    except Exception as e:
        print(e)
        time.sleep(1)
    print(inp)
        

