import numpy as np
import data
import neuralnet

iterations = 9000
learning_rate = 1
norm_rate = 0.0

nn = neuralnet.NeuralNetwork([16,100,4])

try:
	for i in range(iterations):
		nn.learn(data.inputs, data.outputs, learning_rate, norm_rate)
		print(nn.get_errors(data.inputs, data.outputs), '            ', end='\r')
except KeyboardInterrupt:
	print('Learning interrupted')
print()

for val in data.validation:
	output = nn.feed(val[0])
	a = [' '.join(str(int(y)) for y in x) for x in val[0].reshape([4,4]).T.tolist()]
	b = [' '.join(str(int(y)) for y in x) for x in val[1].reshape([2,2]).tolist()]
	c = [' '.join(str(int(y)) for y in x) for x in np.round(output).reshape([2,2]).tolist()]
	a[2] += '\t\t{}\t\t{}'.format(b[0], c[0])
	a[3] += '\t\t{}\t\t{}'.format(b[1], c[1])
	print('\n'.join(a))
	print('-'*40)
