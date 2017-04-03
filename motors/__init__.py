# -*- coding: utf-8 -*-

from .motor import Motor

class MotorController:
	def __init__(self, pin_dx, pin_sx):
		self.mdx = Motor(pin_dx, True)
		self.msx = Motor(pin_sx, False)

	def walk(self, speed, steer):
		if -100 <= speed <= 100 and -100 <= steer <= 100:
			msx_speed = speed + steer
			mdx_speed = speed - steer
			maxSpeed = max(msx_speed, mdx_speed)
			minSpeed = min(msx_speed, mdx_speed)
			if maxSpeed > 100:
				offset = maxSpeed - 100
				msx_speed -= offset
				mdx_speed -= offset
			if minSpeed < -100:
				offset = minSpeed + 100
				msx_speed += offset
				mdx_speed += offset
			self.mdx.set_speed(mdx_speed)
			self.msx.set_speed(msx_speed)
