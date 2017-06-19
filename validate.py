import numpy as np
from neuralnet import NeuralNetwork
import data

nn = NeuralNetwork([10000, 100, 7])

nn.weights = list(np.load('weights.npy'))

for val in data.validation:
	print(val[0], list(nn.feed(val[1]).A.flatten()))
