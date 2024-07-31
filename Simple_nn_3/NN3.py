import sys
import numpy as np
import matplotlib as mlt

input = [1,2,3,2.5]

weights1 = [.2,.8,-.5,1.0]
weights2 = [.5,-0.91,0.26,-0.5]
weights3 = [-.26,-.27,.17,.87]

weights = [weights1,weights2,weights3]

bias1 = 2
bias2 = 3
bias3 = .5

bias = [bias1,bias2,bias3]

""" layer_output = []
for n_weights,n_bias_ in zip(weights,bias):
    neuron_output = 0
    for x,y in zip(input,n_weights):
        neuron_output+=x*y
    neuron_output+=n_bias_
    layer_output.append(neuron_output)

print(layer_output) """

output = np.dot(weights,input) + bias
print(output)