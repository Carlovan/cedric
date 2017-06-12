import numpy as np
import random

all_inputs = []
all_outputs = []

for q in range(4):
	X = q%2  * 2
	Y = q//2 * 2 
	for n in range(1, 17):
		c = '{0:0>4}'.format(bin(n)[2:])
		tmp = np.matrix(np.zeros([4, 4]))
		for i in range(4):
			if c[i] == '1':
				x = i%2
				y = i//2
				tmp[X+x, Y+y] = 1
		all_inputs.append(tmp.flatten().T)
		tmpo = np.matrix(np.zeros([4,1]))
		tmpo[q,0] = 1
		all_outputs.append(tmpo)
all_ = list(zip(all_inputs,all_outputs))

learning = random.sample(all_, 20)
inputs = [x[0] for x in learning]
outputs = [x[1] for x in learning]

validation = random.sample(all_, 10)

extra_inputs = [np.matrix([[0,0,1,1],[0,0,0,0],[1,0,0,0],[0,0,0,0]]).flatten().T]
extra_outputs = [np.matrix([[0,1],[1,0]]).flatten().T]

validation += list(zip(extra_inputs, extra_outputs))
val_inputs = [x[0] for x in validation]
val_outputs = [x[1] for x in validation]
