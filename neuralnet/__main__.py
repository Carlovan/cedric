import numpy as np
import neuralnet

net_size = [10000, 100, 11]
weights_filename = 'weights.npy'

class NNServer:
	def __init__(self):
		self.nn = neuralnet.NeuralNetwork(net_size)
		self.nn.weights = list(np.load(weights_filename))

	def calculateSteering(self, image):
		inputs = np.matrix(image).T
		outputs = self.nn.feed(inputs)
		steering = 0
		outputs = list(outputs.A.flatten())
		for i in range(len(outputs)):
			steering += i * outputs[i]
		steering /= sum(outputs) * len(outputs)
		return steering * 2 - 1
			
