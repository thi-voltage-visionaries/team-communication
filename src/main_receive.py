#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import sx126x
import threading
import time
import select
import termios
import tty
from threading import Timer

old_settings = termios.tcgetattr(sys.stdin)
tty.setcbreak(sys.stdin.fileno())


#
#    Need to disable the serial login shell and have to enable serial interface 
#    command `sudo raspi-config`
#    More details: see https://github.com/MithunHub/LoRa/blob/main/Basic%20Instruction.md
#
#    When the LoRaHAT is attached to RPi, the M0 and M1 jumpers of HAT should be removed.
#

node = sx126x.sx126x(serial_num = "/dev/ttyAMA0",freq=868,addr=0,power=22,rssi=True,air_speed=2400,relay=False)

try:
    time.sleep(1)
    while True:
        test = node.receive()
        if test != None:

            print("Received from sx126x: ",test)
except:
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
    # print('\x1b[2A',end='\r')
    # print(" "*100)
    # print(" "*100)
    # print('\x1b[2A',end='\r')

termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
# print('\x1b[2A',end='\r')
# print(" "*100)
# print(" "*100)
# print('\x1b[2A',end='\r')
