# -*- coding: utf-8 -*-

from .motor import Motor
import zerorpc

class MotorController:
	def __init__(self, pin_dx, pin_sx):
		self.mdx = Motor(pin_dx, True)
		self.msx = Motor(pin_sx, False)

	def walk(self, speed, steer):
		if -100 <= speed <= 100 and -100 <= steer <= 100:
			msx_speed = speed + steer
			mdx_speed = speed - steer
			tmp1 = max(msx_speed, mdx_speed)
			tmp2 = min(msx_speed, mdx_speed)
			if tmp1 > 100:
				offset = tmp1 - 100
				msx_speed -= offset
				mdx_speed -= offset
			if tmp2 < -100:
				offset = tmp2 + 100
				msx_speed += offset
				mdx_speed += offset
			self.mdx.SetSpeed(mdx_speed)
			self.msx.SetSpeed(msx_speed)

server = zerorpc.Server(MotorController(4, 5))
server.bind('tcp://127.0.0.1:22000')
server.run()
