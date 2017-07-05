import numpy as np
from neuralnet import NeuralNetwork
import data

nn = NeuralNetwork([10000, 100, 7])

nn.weights = list(np.load('weights.npy'))

results = []
for val in data.validation:
	results.append([val[0], list(nn.feed(val[1]).A.flatten())])

results.sort(key=lambda x: x[0])
print('\n'.join('{}: {}'.format(x[0], x[1]) for x in results))
