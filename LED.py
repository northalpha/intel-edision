#!/usr/bin/python
#
# Stefan Kloepping <northalpha@c3pb.de>
#  --  Do 26 Nov 00:01:51 2015
#

import pyupm_i2clcd as lcd
import mraa
import time
import sys

# Initialize Jhd1313m1 at 0x3E (LCD_ADDRESS) and 0x62 (RGB_ADDRESS)
myLcd = lcd.Jhd1313m1(0, 0x3E, 0x62)

while True:

	# Green
	myLcd.setColor(102, 0, 102)

	# Zero the cursor
	myLcd.setCursor(0,0)

	# Print it.
	text = str('Hallo Welt')
	myLcd.write(text)
	
	# Second row
	myLcd.setCursor(1,0)
	myLcd.write('second line')

	time.sleep(1)