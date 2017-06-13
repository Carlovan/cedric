import RPi.GPIO as GPIO

def scale(value, oldL, oldR, newL, newR):
	return (value - oldL) / (oldR - oldL) * (newR -  newL) + newL

class Motor:
	_mult = 1
	def __init__(self, pin, rev=False, offset=0):
		# Class constructor
		# Offset is used to calibrate the motor

		# Make sure the pin is in output mode
		GPIO.cleanup(pin)
		GPIO.setup(pin, GPIO.OUT)

		if rev == True:
			self._mult = -1

		self.pin = pin
		self.offset = offset
		self.pwmHandler = GPIO.PWM(pin, 50)
		self.pwmHandler.start(0)

	def __del__(self):
		# Class destructor
		self.pwmHandler.stop()

	def set_speed(self, speed):
		# Sets the speed of the motor.
		# The parameter must be between -100.0 and 100.0 (included)
		assert(-1 <= speed <= 1)
		speed *= self._mult
		speed += self.offset
		#dc = scale(speed, -1, 1, 4.7954, 9.7954)
		dc = scale(speed, -1, 1, 5, 10)
		self.pwmHandler.ChangeDutyCycle(dc)
