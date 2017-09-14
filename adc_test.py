# -*- coding: utf-8 -*-
#!/usr/bin/env python

#using adc by zerogpio

from gpiozero import MCP3204
from time import sleep

adc = MCP3204(channel = 0) # channel selection

while True:
	print(str(adc.value*61+2))
	sleep(0.5)
