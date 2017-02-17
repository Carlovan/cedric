import RPi.GPIO as GPIO
import time
from motor import Motor

pin = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)
GPIO.setwarnings(False)

mm = Motor(pin)

try:
	while True:
		tmp = input()
		dc = float(tmp)
		mm.SetSpeed(dc)

except KeyboardInterrupt:
	pass
finally:
	GPIO.cleanup()
	print('\rInterrupt received, exiting')
