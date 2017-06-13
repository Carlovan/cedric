import zerorpc
from motors import MotorController
import RPi.GPIO as GPIO

pin1 = 3
pin2 = 4

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(pin1, GPIO.OUT)
GPIO.setup(pin2, GPIO.OUT)

server = zerorpc.Server(MotorController(pin1, pin2))
server.bind('ipc:///tmp/22000')
server.run()
