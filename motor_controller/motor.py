import RPi.GPIO as GPIO

def scale(value, oldL, oldR, newL, newR):
	return (value - oldL) / (oldR - oldL) * (newR -  newL) + newL

class Motor:
	_mult = 1
	def __init__(self, pin, rev=False):
		# Class constructor

		# Make sure the pin is in output mode
		GPIO.cleanup(pin)
		GPIO.setup(pin, GPIO.OUT)

		if rev == True:
			self._mult = -1

		self.pin = pin
		self.pwmHandler = GPIO.PWM(pin, 50)
		self.pwmHandler.start(0)

	def __del__(self):
		# Class destructor
		self.pwmHandler.stop()

	def SetSpeed(self, speed):
		# Sets the speed of the motor.
		# The parameter must be between -100.0 and 100.0 (included)

		speed *= self._mult
		
		if not -100.0 <= speed <= 100.0:
			raise ValueError('Must be -100.0 <= speed <= 100')

		dc = scale(speed, -100, 100, 5, 10)
		self.pwmHandler.ChangeDutyCycle(dc)
		if speed == 0:
			self.pwmHandler.ChangeDutyCycle(0) # The motor is REALLY stopped
