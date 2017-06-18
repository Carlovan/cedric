import zerorpc
import camera
import time

camera.init()

class CameraController():
	def shoot(self):
		filename = '/tmp/image.dat'
		with open(filename, 'wb') as f:
			f.write(bytearray(camera.shoot().flatten().tolist()))
		return filename

server = zerorpc.Server(CameraController(), pool_size=2)
server.bind('tcp://127.0.0.1:22001')
print('Running!')
server.run()
