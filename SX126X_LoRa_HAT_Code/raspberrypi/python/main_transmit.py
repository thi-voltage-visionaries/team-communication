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
import json
from glob import glob
import os

json_directory = '/home/test/Desktop/team-bms/battery_data_json'
last_file = None
seconds = 5

old_settings = termios.tcgetattr(sys.stdin)
tty.setcbreak(sys.stdin.fileno())


#
#    Need to disable the serial login shell and have to enable serial interface 
#    command `sudo raspi-config`
#    More details: see https://github.com/MithunHub/LoRa/blob/main/Basic%20Instruction.md
#
#    When the LoRaHAT is attached to RPi, the M0 and M1 jumpers of HAT should be removed.
#


# Funktion um die neueste JSON-Datei zu finden
def get_latest_json_file():
    files = glob(os.path.join(json_directory, "battery_data_*.json"))
    if not files:
        return None
    latest_file = max(files, key=os.path.getctime)
    global last_file
    if latest_file == last_file:
        return None
    last_file = latest_file
    return latest_file

#   Read an json file and send the data once to another node
def send_json_file():
    with open(get_latest_json_file(), 'r') as f:
        data = json.load(f)

    data = bytes([255]) + bytes([255]) + bytes([18]) + bytes([255]) + bytes([255]) + bytes([12]) + "Battery Data:".encode()+str(data).encode()
    node.send(data)
    time.sleep(0.2)

def send_json_file_continue(continue_or_not = True):
    if continue_or_not:
        global timer_task
        global seconds
        # send only if there is a new file
        if get_latest_json_file() != None:
            with open(get_latest_json_file(), 'r') as f:
                data = json.load(f)
            data = bytes([255]) + bytes([255]) + bytes([18]) + bytes([255]) + bytes([255]) + bytes([12]) + "Battery Data:".encode()+str(data).encode()
            node.send(data)
        else:
            print("No new file found")
        time.sleep(0.2)
        timer_task = Timer(seconds,send_json_file_continue)
        timer_task.start()
    else:
        with open('battery_data.json', 'r') as f:
            data = json.load(f)
        data = bytes([255]) + bytes([255]) + bytes([18]) + bytes([255]) + bytes([255]) + bytes([12]) + "Battery Data:".encode()+str(data).encode()
        node.send(data)
        time.sleep(0.2)
        timer_task.cancel()
        pass

node = sx126x.sx126x(serial_num = "/dev/ttyAMA0",freq=868,addr=34,power=22,rssi=True,air_speed=2400,relay=False)

# comment out if you want to select the sending mode
#----------------------------------------------------
timer_task = Timer(seconds,send_json_file_continue)
timer_task.start()
#----------------------------------------------------

'''
try:
    time.sleep(1)
    print("Press \033[1;32mEsc\033[0m to exit")
    print("Press \033[1;32mi\033[0m   to send")
    print("Press \033[1;32ms\033[0m   to send data every 5 seconds")
    
    # it will send rpi cpu temperature every 10 seconds 
    seconds = 5
    
    while True:

        if select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], []):
            c = sys.stdin.read(1)

            # dectect key Esc
            if c == '\x1b': break
            # dectect key i
            if c == '\x69':
                send_json_file()
                #send_deal()
            # dectect key s
            if c == '\x73':
                print("Press \033[1;32mc\033[0m   to exit the send task")
                timer_task = Timer(seconds,send_json_file_continue)
                timer_task.start()
                
                while True:
                    if sys.stdin.read(1) == '\x63':
                        timer_task.cancel()
                        print('\x1b[1A',end='\r')
                        print(" "*100)
                        print('\x1b[1A',end='\r')
                        break

            sys.stdout.flush()
            
        node.receive()
        
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
'''
