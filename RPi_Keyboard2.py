##!/usr/bin/env python3
#from adafruit_hid.keycode import Keycode
from Keyboard_us import KeyboardLayoutUS
kb = KeyboardLayoutUS()

NULL_CHAR = chr(0)
import time
class Keyboard():
    def __init__(self):
        pass

    def __write_report(report):
        with open('/dev/hidg0', 'rb+') as fd:
            fd.write(report.encode())
    time.sleep(2)
    def keyout(self,k):
        for i in k:
            key = kb.keycodes(i)
            self.__write_report(chr(key[0])+NULL_CHAR+chr(key[1])+NULL_CHAR*5)
            self.__write_report(NULL_CHAR*8)
        self.__write_report(NULL_CHAR*2+chr(kb.keycodes('\n')[1])+NULL_CHAR*5)
        self.__write_report(NULL_CHAR*8)

# Press a
#write_report(NULL_CHAR*2+chr(4)+NULL_CHAR*5)
# Release keys
#write_report(NULL_CHAR*8)
# Press SHIFT + a = A
#write_report(chr(32)+NULL_CHAR+chr(4)+NULL_CHAR*5)

#write_report(NULL_CHAR*8)

if __name__ == '__main__':
    kb = Keyboard()
    kb.keyout('Hello World 111')

