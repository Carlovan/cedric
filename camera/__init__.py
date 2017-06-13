import numpy as np
import zerorpc
import picamera
from math import ceil

_camera = None
_res = (50, 50)
_buffer_size = (ceil(_res[0] / 32) * 32, ceil(_res[1] / 16) * 16, 3)

def init():
	global _camera
	_camera = picamera.PiCamera()
	_camera.framerate = 90
	_camera.resolution = _res

def shoot():
	output = np.empty(_buffer_size, dtype=np.uint8)
	_camera.capture(output, 'rgb')
	output = output[:_res[0], :_res[1], :]
	return output
