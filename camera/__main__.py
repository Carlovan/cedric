import zerorpc
import camera

camera.init()

class CameraController():
	def shoot(self):
		return camera.shoot().tolist()

server = zerorpc.Server(CameraController(), pool_size=2)
server.bind('ipc:///tmp/22001')
print('Running!')
server.run()
