#!/usr/bin/python
# -*- coding: UTF-8 -*-

#    Need to disable the serial login shell and have to enable serial interface 
#    command `sudo raspi-config`
#    More details: see https://github.com/MithunHub/LoRa/blob/main/Basic%20Instruction.md
#
#    When the LoRaHAT is attached to RPi, the M0 and M1 jumpers of HAT should be removed.

import sx126x
import time
from threading import Timer
import json
from glob import glob
import os

json_directory = '/home/test/Desktop/team-bms/battery_data_json'
last_file = None

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


node = sx126x.sx126x(serial_num = "/dev/ttyAMA0",freq=868,addr=34,power=22,rssi=True,air_speed=2400,relay=False)

time.sleep(5)

while True:
    latest_json_file = get_latest_json_file()
    if latest_json_file != None:
        with open(latest_json_file, 'r') as f:
            data = json.load(f)
        data = bytes([255]) + bytes([255]) + bytes([18]) + bytes([255]) + bytes([255]) + bytes([12]) + "Battery Data:".encode()+str(data).encode()
        node.send(data)
        print("New data sent")
    else:
        print("No new data to send")
    time.sleep(10)

