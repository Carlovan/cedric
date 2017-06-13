import zerorpc
import camera

camera.init()

class CameraController():
	def shoot(self):
		return camera.shoot().tolist()

server = zerorpc.Server(CameraController())
server.bind('tcp://127.0.0.1:22001')
server.run()
