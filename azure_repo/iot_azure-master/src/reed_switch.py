"""
================================================================================
Author:      Stepan Gaponiuk - D ONE 2023
Description: This script blinks the LED when reed switch is engaged
================================================================================
"""
import time
import sys
import RPi.GPIO as io
import json
from user_input import LED_PIN, SWITCH_PIN

# Set Broadcom mode so we can address GPIO pins by number.
io.setmode(io.BCM)
io.setup(SWITCH_PIN, io.IN, pull_up_down=io.PUD_UP)
io.setup(LED_PIN, io.OUT)

magnet = 0

def iothub_client_telemetry_sample_run():

    try:
        print ( "Touch the Reed switch with the magnet to make LED blink, press Ctrl-C to exit" )
        while True:
            time.sleep(1)
            if (io.input(SWITCH_PIN) == 0):
                magnet = 1
                io.output(LED_PIN, io.HIGH)
                print( "LED is ON!" )
            else:
                magnet = 0
                io.output(LED_PIN, io.LOW)
                print( "LED is OFF!" )

    except KeyboardInterrupt:
        print ( "LED blinking script is stopped" )
        io.cleanup()
        sys.exit()

if __name__ == '__main__':
    print ( "LED blinking script - Raspberry PI device" )
    print ( "Press Ctrl-C to exit" )
    iothub_client_telemetry_sample_run()