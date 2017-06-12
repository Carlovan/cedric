import numpy as np

def add_bias(mat):
	return np.append([[1]], mat, axis=0)

class NeuralNetwork:
	def __init__(self, sizes):
		# Sizes is a tuple of int, each one is the size of a layer
		self.weights = [] # weights[n] are the weights between layers n and n+1
		for i in range(len(sizes)-1):
			curr_l = sizes[i]+1 # Size of the current layer (added bias)
			next_l = sizes[i+1]  # Size of the next layer
			tmp_w = np.matrix(np.random.random([next_l, curr_l]) * 2 - 1) # The mean is 0 
			self.weights.append(tmp_w)

	def feed(self, input_val):
		# Feeds the network with the given inputs and calculates the outputs
		assert(type(input_val) is np.matrix)
		curr_layer = np.matrix(input_val) # Create a new copy (not only reference)
		layers = [curr_layer]
		for syn in self.weights:
			curr_layer = add_bias(curr_layer)
			curr_layer = syn.dot(curr_layer) # Calculate the next layer
			layers.append(curr_layer)
		return layers[-1]
