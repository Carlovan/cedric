import numpy as np
import zerorpc
import picamera
from math import ceil
import time
import cv2

_camera = None
_res = (200, 200)
_buffer_size = (ceil(_res[1] / 16) * 16, ceil(_res[0] / 32) * 32, 3)
print(_buffer_size)

def init():
	global _camera
	_camera = picamera.PiCamera()
	_camera.rotation = 180
	_camera.resolution = _res
	time.sleep(2)

def shoot():
	output = np.empty(_buffer_size, dtype=np.uint8)
	_camera.capture(output, 'bgr')
	output = output[:_res[1], :_res[0], :]
	return cv2.cvtColor(output, cv2.COLOR_BGR2GRAY)
