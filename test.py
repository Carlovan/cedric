import RPi.GPIO as GPIO
import time
import motors

pin1 = 3
pin2 = 4

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(pin1, GPIO.OUT)
GPIO.setup(pin2, GPIO.OUT)

mc = motors.MotorController(pin1, pin2)
try:
	while True:
		tmp = input().split()
		speed = float(tmp[0])
		steer = float(tmp[1])
		mc.walk(speed, steer)

except KeyboardInterrupt:
	pass
finally:
	GPIO.cleanup()
	print('\rInterrupt received, exiting')
