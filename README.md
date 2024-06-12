# Communication Team

## Description
This Repository contains all files to send files from a serial connected LORA device to the Azure IOT hub.<br>
In our Use case we use it to upload BMS Data to the Azure IOT Hub. <br>


## Hardware

Lora Module: https://www.waveshare.com/wiki/SX1262_868M_LoRa_HAT <br>
Raspberry Pi 5: https://www.raspberrypi.com/products/raspberry-pi-5/

## Installation on RPi:
Enable serial port: <br>
`sudo raspi-config`
-> Interfacing Options -> Serial -> No -> Yes

Install the Services: <br>
On the Transmitter RPi connected to the BMS install the `main_transmitter.service` into the `/etc/systemd/system/` folder. <br>
On the Receiver RPi install the `main_receiver.service` into the `/etc/systemd/system/` folder.

Configure the Services: <br>
On the TX RPi run `sudo systemctl enable main_transmitter.service` <br>
On the RX RPi run `sudo systemctl enable main_receiver.service`

## Set Jumpers
![SX1268_LoRa_HAT](SX1268_LoRa_HAT.png)

10: UART selection jumpers
- A: control the LoRa module through USB TO UART
- B: control the LoRa module through Raspberry Pi
- C: access Raspberry Pi through USB TO UART

11: LoRa mode selection jumpers
(Don't set the jumper if the LoRa module is set up by the Raspberry Pi)
- short M0, short M1: transmission mode
- short M0, open M1: configuration mode
- open M0, short M1: WOR mode
- open M0, open M1: deep sleep mode
