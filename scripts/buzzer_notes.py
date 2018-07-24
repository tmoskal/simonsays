import RPi.GPIO as GPIO
import time
import random

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

buzz_pin = 32

GPIO.setup(buzz_pin,GPIO.OUT)
Buzz = GPIO.PWM(buzz_pin,1000)

frequencies = [69,25,178,100]
n = random.randint (0,3)
Buzz.ChangeFrequency(frequencies[n])
Buzz.start(10)
time.sleep(0.5)
Buzz.stop()



