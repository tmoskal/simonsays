import LEDRGB as LED
import RPi.GPIO as GPIO
import time
import random
colors = ['R','G','B','Y', 'C','P','O','D']
R_pin = 11
G_pin = 12
B_pin = 13
LED.setup(R_pin,G_pin,B_pin)
def simonsays():
	while True:
		n = random.randint(0,3)
		LED.setColor(colors[n])
		time.sleep(.5)
if __name__ == '__main__':
	try:
		simonsays()
	except KeyboardInterrupt:
		print 'Good bye'
		LED.destroy()
