	#!/usr/bin/python
	#
	# Stefan Kloepping <northalpha@c3pb.de>
	#  --  Do 26 Nov 17:27:27 2015
	#
	import pyupm_i2clcd as lcd
	import pyupm_grove
	import time

	# define that Light Sensor is on A0
	light = pyupm_grove.GroveLight(0)

	# initiale LCD display
	myLcd = lcd.Jhd1313m1(0, 0x3E, 0x62)

	while True:
		
		# Green
		myLcd.setColor(255, 255, 0)

		# Zero the cursor
		myLcd.setCursor(0,0)

		# Print first line with light value in Lux:
		text = str('Lux Wert: ') + str(light.value())
		myLcd.write(text)
		time.sleep(1)