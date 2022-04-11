# pi-neomatrix
multipurpose LED display driven by raspberry pi
# Features
## Hardware Setup ##
Required hardware:

- Raspberry Pi 3 B+
- HW-221 Level shifter
- 16x16 WS2812 matrix
- INMP441 I2S MEMS Microphone
- BH1750 Light sensor
- MLX90640 IR Thermal Camera

## Sofware Setup ##
To get started, set up a Raspberry Pi using the Raspian lite OS and connect it to your network using `raspi-config`. In raspi-config, go to interface and enable SSH, I2C, and SPI, then connect to WiFi.

Run `sudo apt-get update` to update the OS and then ensure SSH access before disconnecting the Raspberry Pi from your display if you wish to use the device remotely. 
Run `sudo apt install python3-pip` to get pip 

`sudo pip3 install -r requirements.txt`

Numpy for raspberry pi
sudo apt-get install libopenjp2-7

Setting up the I2S microphone:
https://learn.adafruit.com/adafruit-i2s-mems-microphone-breakout/raspberry-pi-wiring-test

Installing pyaudio:
$ sudo apt-get install git
$ git clone http://people.csail.mit.edu/hubert/git/pyaudio.git
$ sudo apt-get install libportaudio0 libportaudio2 libportaudiocpp0 portaudio19-dev
$ sudo apt-get install python-dev
$ cd pyaudio
$ sudo python setup.py install
