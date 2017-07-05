import zerorpc
import numpy as np
import neuralnet

net_size = [10000, 100, 11]
weights_filename = 'weights.npy'

class NNServer:
	def __init__(self):
		self.nn = neuralnet.NeuralNetwork(net_size)
		self.nn.weights = list(np.load(weights_filename))

	def calculateSteering(self, image):
		inputs = np.array(bytearray(image), dtype=np.float64)
		inputs = np.matrix(inputs / 255).T
		outputs = self.nn.feed(inputs)
		steering = 0
		outputs = list(outputs.A.flatten())
		for i in range(len(outputs)):
			steering += i * outputs[i]
		steering /= sum(outputs) * len(outputs)
		return steering * 2 - 1

server = zerorpc.Server(NNServer())
server.bind('tcp://127.0.0.1:22002')
print('Running')
server.run()
