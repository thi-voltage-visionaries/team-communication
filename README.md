# Communication Team

## Description
This Repository contains all files to send files from a serial connected LORA device to the Azure IOT hub.<br>
In our Use case we use it to upload BMS Data to the Azure IOT Hub. <br>

## Hardware
Lora Module: https://www.waveshare.com/wiki/SX1262_868M_LoRa_HAT <br>
Raspberry Pi 5: https://www.raspberrypi.com/products/raspberry-pi-5/

## Installation on RPi:

clone the repository into the home directory:<br>
`git clone git@github.com:thi-voltage-visionaries/team-communication.git`
 
1. Enable the gpio serial port: <br>
`sudo raspi-config`
-> Interfacing Options -> Serial -> No -> Yes

2. Install the Services: <br>
On the Transmitter RPi connected to the BMS install the `transmit.service` into the `/etc/systemd/system/` folder. <br>
`mv team-communication/ServiceFiles/transmit.service /etc/systemd/system/`<br>
On the Receiver RPi install the `receive.service` into the `/etc/systemd/system/` folder.<br>
`mv team-communication/ServiceFiles/receive.service /etc/systemd/system/`<br>

3. Configure the Services: <br>
On the TX RPi run `sudo systemctl enable transmit.service` <br>
Start transmitter on first run `sudo systemctl start transmit.service`<br>
On the RX RPi run `sudo systemctl enable receive.service`<br>
Start receiver on first run `sudo systemctl start receive.service`<br>

## Lora Hat Configuration

### Set Jumpers
![SX1268_LoRa_HAT](SX1268_LoRa_HAT.png)

UART selection jumpers
- A: control the LoRa module through USB TO UART
- B: control the LoRa module through Raspberry Pi
- C: access Raspberry Pi through USB TO UART

LoRa mode selection jumpers
- short M0, short M1: transmission mode
- short M0, open M1: configuration mode
- open M0, short M1: WOR mode
- open M0, open M1: deep sleep mode
- If the Python script on the Raspberry pi is used the jumpers don't need to be connected at all, because the GPIOs on the Raspberry configure the pins as needed

## Connect to Raspberry Pis

### Wifi Config
The Raspberries are set up to connect to a specific wifi network:
SSID: batteryproject
PW: batteryproject

### SSH
The transmit RPi has the hostname `bp1` and username `test`<br>
The receive RPi has the hostname `bp2` and username `bp2`<br>

Connecting can be done over SSH<br>
`ssh test@bp1`<br>
`ssh bp2@bp2`<br>
