#!/usr/bin/env python3

from time import sleep
import board
import busio
import digitalio
import adafruit_mcp3xxx.mcp3008 as MCP3008
from adafruit_mcp3xxx.analog_in import AnalogIn
import RPi.GPIO

SPI = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
MCP3008_CS = digitalio.DigitalInOut(board.D22)
MCP3008_SPI = MCP3008.MCP3008(SPI, MCP3008_CS)
ADC_CH0 = AnalogIn(MCP3008_SPI, MCP3008.P0)
ADC_CH1 = AnalogIn(MCP3008_SPI, MCP3008.P1)
ADC_DIFF = AnalogIn(MCP3008_SPI, MCP3008.P1, MCP3008.P0)

print("Press CTRL-C to exit.")
try:
    while True:
        print(f"ADC  CH0: {ADC_CH0.voltage:4.2f} V ({ADC_CH0.value:5d})")
        print(f"ADC  CH1: {ADC_CH1.voltage:4.2f} V ({ADC_CH1.value:5d})")
        print(f"ADC DIFF: {ADC_DIFF.voltage:4.2f} V ({ADC_DIFF.value:5d})")
        print()
        sleep(0.1)
except KeyboardInterrupt:
    RPi.GPIO.cleanup()
    print("\nCleaned up GPIO resources.")
