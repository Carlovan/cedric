# -*- coding: utf-8 -*-

from .motor import Motor

class MotorController:
	def __init__(self, pin_dx, pin_sx):
		self.mdx = Motor(pin_dx, True)
		self.msx = Motor(pin_sx, False)

	def walk(self, speed, steer):
		if -1 <= speed <= 1 and -1 <= steer <= 1:
			msx_speed = speed + steer*speed
			mdx_speed = speed - steer*speed
			self.mdx.set_speed(mdx_speed)
			self.msx.set_speed(msx_speed)
			print('Speed:', speed, 'Steer:', steer, end='\r')
		return 'ok'
