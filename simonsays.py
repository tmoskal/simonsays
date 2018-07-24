import LEDRGB as LED
import RPi.GPIO as GPIO
import time
import random

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

buzz_pin = 32

colors = ['R','G','B','Y', 'C','P','O','D']
frequencies = [220,660,880,440,330,550,770,110]
colorlist = []
soundlist = []
R_pin = 11
G_pin = 12
B_pin = 13
GPIO.setup(buzz_pin,GPIO.OUT)
Buzz = GPIO.PWM(buzz_pin,1000)
LED.setup(R_pin,G_pin,B_pin)
def simonsays():
	while True:
		n = random.randint(0,3)
		colorlist.append(colors[n])
		soundlist.append(frequencies[n])
		p = len(colorlist)
		x = 0
		while p > 0:
			LED.setColor(colorlist[x])
			Buzz.ChangeFrequency(soundlist[x])
			Buzz.start(1)
			time.sleep(.5)
			Buzz.stop()
			LED.noColor()
			time.sleep(.5)
			p = p - 1
			x = x + 1
			
if __name__ == '__main__':
	try:
		simonsays()
	except KeyboardInterrupt:
		print 'Good bye'
		LED.destroy()
