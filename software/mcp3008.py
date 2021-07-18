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

currenttime=0
waittime = 1/150
lastbit = 0
hz=0

totalcounts=0
tally=0

print("Press CTRL-C to exit.")
try:
	while True:
		#print(f"ADC  CH0: {ADC_CH0.voltage:4.2f} V ({ADC_CH0.value:5d})")
		#print()
		ledon = ADC_CH0.voltage > 1.5
		if lastbit != ledon:
			hz += 1
			lastbit = ledon

		sleep(waittime)
		currenttime += 1
		if currenttime == 150:
			#ms = (0.95*hz) + 0.35
			rs = hz + 1.0

			ms = rs*0.095
			tally+=ms
			totalcounts+=1
			print(f"Speed: {ms:4.2f} m/s")
			hz=0
			currenttime = 0
except KeyboardInterrupt:
	RPi.GPIO.cleanup()
	print("\nCleaned up GPIO resources.")
	print(f"Average: {tally/totalcounts:4.2f}")
