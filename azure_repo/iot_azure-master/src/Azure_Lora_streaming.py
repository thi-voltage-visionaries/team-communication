"""
================================================================================
Author:      Stepan Gaponiuk - D ONE 2023
Description: This script blinks the LED when reed switch is engaged and sends data to Azure IoT Hub
================================================================================
"""
import time
import sys
import RPi.GPIO as io
import json
from user_input import LED_PIN, SWITCH_PIN, IOT_HUB_CON_STR, DEVICE_ID
from azure.iot.device import IoTHubDeviceClient, Message

# lora dependencies
import sx126x

# create lora receiver node
node = sx126x.sx126x(serial_num = "/dev/ttyAMA0",freq=868,addr=0,power=22,rssi=True,air_speed=2400,relay=False)

# Set Broadcom mode so we can address GPIO pins by number.
io.setmode(io.BCM)
io.setup(SWITCH_PIN, io.IN, pull_up_down=io.PUD_UP)
io.setup(LED_PIN, io.OUT)

# Define the JSON message variables to send to IoT Hub.
messageEpoch = time.time()
magnet = 0

def iothub_client_init():
    # Create an IoT Hub client using protocol MQTT v3.1.1 over WebSocket on port 443.
    client = IoTHubDeviceClient.create_from_connection_string(IOT_HUB_CON_STR, websockets=True) 
    return client

def iothub_client_telemetry_sample_run():

    try:
        client = iothub_client_init()
        print ( "IoT Hub device sending periodic messages, press Ctrl-C to exit" )
        while True:
            # Build the message with magnet telemetry values.
            messageEpoch = time.time()
            time.sleep(1)
            magnet = 1
            io.output(LED_PIN, io.HIGH)

            # with open('/home/bp1/azure_repo/iot_azure-master/src_new/battery_data/battery_data_1714051530.json', 'r') as f:
            #    data = json.load(f)

            # message = Message(json.dumps(data))

            #msg_dict = {"messageEpoch":messageEpoch, "deviceID":DEVICE_ID, "magnet":magnet, "pin_num":SWITCH_PIN}
            #message = Message(json.dumps(msg_dict))

            # receive data from lora
            loraData = node.receive()
            if loraData != None:
                message = Message(loraData)

                # ensure proper encoding and content type are enforced (again to avoid de-serialization issues)
                message.content_encoding = "utf-8"
                message.content_type = "application/json"

                # Send the message.
                print( "Sending message: {}".format(message) )
                client.send_message(message)
                print ( "Message successfully sent" )


    except KeyboardInterrupt:
        print ( "IoTHubClient sample stopped" )
        io.cleanup()
        sys.exit()

if __name__ == '__main__':
    print ( "Azure IoT Medium Post - Raspberry PI device" )
    print ( "Press Ctrl-C to exit" )
    iothub_client_telemetry_sample_run()
