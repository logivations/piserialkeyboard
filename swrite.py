import time
import serial
          
      
ser = serial.Serial(
              
               port='/dev/ttyS0',
               baudrate = 115200,
               parity=serial.PARITY_NONE,
               stopbits=serial.STOPBITS_ONE,
               bytesize=serial.EIGHTBITS,
               timeout=1
           )
while 1:
               i = input('message to send-->')
               ser.write(i.encode())
               time.sleep(.01)
               if i=='q':break
