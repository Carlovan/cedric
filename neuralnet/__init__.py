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
		curr_layer = input_val.copy() # Create a new copy (not only reference)
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
		return DELTA
	
	def learn(self, input_vals, output_vals, learning_rate, norm_rate):
		D = None
		for i in range(len(input_vals)):
			tmp = self._calculate_backprop(input_vals[i], output_vals[i])
			if D is None:
				D = tmp
			else:
				for j in range(len(D)):
					D[j] += tmp[j]
		tmp_w = self.weights.copy()
		for i in range(len(tmp_w)):
			tmp_w[i][:, 0] = 0 # Zero the first column (bias weight)
		#print(tmp_w)
		for i in range(len(D)):
			D[i] += norm_rate * tmp_w[i]
			D[i] /= len(input_vals)
		for i in range(len(D)):
			self.weights[i] -= learning_rate * D[i]

	def get_error(self, input_val, output_val):
		# Return the mean square error
		assert(type(input_val) is np.matrix)
		assert(type(output_val) is np.matrix)
		output = self.feed(input_val)
		return np.sqrt(np.mean(np.power(output - output_val, 2)))

	def get_errors(self, input_vals, output_vals):
		# Return the mean of the errors for every test case
		total = 0
		for testcase in zip(input_vals, output_vals):
			total += self.get_error(testcase[0], testcase[1])
		return total / len(input_vals)
