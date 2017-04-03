# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import zerorpc
from . import MotorController

try:
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	server = zerorpc.Server(MotorController(3, 4))
	server.bind('tcp://127.0.0.1:22000')
	server.run()
except KeyboardInterrupt:
	print('Exiting...')
finally:
	GPIO.cleanup()
