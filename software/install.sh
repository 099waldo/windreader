#!/bin/bash
# https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/installing-circuitpython-on-raspberry-pi
# https://www.woolseyworkshop.com/2020/11/23/adding-analog-inputs-to-your-raspberry-pi/
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install python3-pip
sudo pip3 install --upgrade setuptools
sudo pip3 install --upgrade adafruit-python-shell
wget https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/raspi-blinka.py
sudo python3 raspi-blinka.py
sudo pip3 install --upgrade Adafruit-Blinka
sudo pip3 install adafruit-circuitpython-mcp3xxx
