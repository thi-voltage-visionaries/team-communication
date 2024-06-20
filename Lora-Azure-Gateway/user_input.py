"""
===================================================================================================
Author:      Stepan Gaponiuk - D ONE 2023
Description: This script contains user input for streaming Raspberry Pi reed signal data into Azure
===================================================================================================
"""

# GPIO
LED_PIN = 4  # GPIO pin where the LED is connected to
SWITCH_PIN = 18  # GPIO pin where the reed switch is connected to

# Azure
# IOT_HUB_CON_STR = "HostName=VVCloudDasboard.azure-devices.net;DeviceId=Raspberry2;SharedAccessKey=YO58Wn/LZWCqkTq+Kl8yWU57KXjmPFcYULJhAX3WMIk="  # Paste your Azure IoT Hub connection string
IOT_HUB_CON_STR = "HostName=VoltageVisionariesWebapp.azure-devices.net;SharedAccessKeyName=iothubowner;SharedAccessKey=lWRMdTmTACTvPq0tyEWIFCjL9zt3jw4jkAIoTFQEvsE="
DEVICE_ID = "Raspberry"  # Paste your Azure IoT Hub device name
