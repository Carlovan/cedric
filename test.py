import time
import motors

pin1 = 3
pin2 = 4

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
	print('\rInterrupt received, exiting')
