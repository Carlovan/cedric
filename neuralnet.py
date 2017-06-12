import numpy as np

def add_bias(mat):
	return np.append([[1]], mat, axis=0)

def remove_bias(mat):
	return np.delete(mat, 0, axis=0)

def sigmoid(x, derivative=False):
	if not derivative:
		return 1 / (1 + np.exp(-x))
	else:
		return np.multiply(x, 1-x) # Element-wise multiplication

class NeuralNetwork:
	def __init__(self, sizes):
		# Sizes is a tuple of int, each one is the size of a layer
		self.weights = [] # weights[n] are the weights between layers n and n+1
		for i in range(len(sizes)-1):
			curr_l = sizes[i]+1 # Size of the current layer (added bias)
			next_l = sizes[i+1]  # Size of the next layer
			tmp_w = np.matrix(np.random.random([next_l, curr_l]) * 2 - 1) # The mean is 0 
			self.weights.append(tmp_w)

	def feed(self, input_val, get_all=False):
		# Feeds the network with the given inputs and calculates the outputs
		# If get_all is True return all the layers, not only the output
		assert(type(input_val) is np.matrix)
		curr_layer = np.matrix(input_val) # Create a new copy (not only reference)
		layers = [curr_layer]
		for syn in self.weights:
			curr_layer = add_bias(curr_layer)
			curr_layer = sigmoid(syn.dot(curr_layer)) # Calculate the next layer
			layers.append(curr_layer)
		if get_all == True:
			return layers
		else:
			return layers[-1]

	def _calculate_backprop(self, input_val, output_val):
		assert(type(input_val) is np.matrix)
		assert(type(output_val) is np.matrix)
		layers = self.feed(input_val, get_all=True) # Perform forward propagation
		delta = [None] * (len(self.weights) + 1)

		delta[-1] = layers[-1] - output_val
		for i in range(len(delta) - 2, 0, -1): # Iterate over layers backward
			cur_delta = remove_bias(self.weights[i].T.dot(delta[i+1]))
			delta[i] = np.multiply(cur_delta, sigmoid(layers[i], derivative=True))

		DELTA = [None] * len(self.weights)
		for i in range(len(delta) - 1):
			DELTA[i] = delta[i+1].dot(add_bias(layers[i]).T)
		print('\n'.join([str(x.shape) for x in self.weights]))
		print('-'*40)
		print('\n'.join([str(x.shape) for x in DELTA]))
		return DELTA
