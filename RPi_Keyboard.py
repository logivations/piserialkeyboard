#!/usr/bin/env python3
NULL_CHAR = chr(0)
import time
def write_report(report):
    with open('/dev/hidg0', 'rb+') as fd:
        fd.write(report.encode())
time.sleep(2)
# Press a
write_report(NULL_CHAR*2+'A'+NULL_CHAR*5)
# Release keys
write_report(NULL_CHAR*8)
# Press SHIFT + a = A
write_report(chr(32)+NULL_CHAR+chr(4)+NULL_CHAR*5)

write_report(NULL_CHAR*8)
