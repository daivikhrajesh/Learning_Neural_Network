import random
import numpy as np
import matplotlib as mlt

X = [[1, 2, 3, 2.5],
     [2.0, 5.0, -1.0, 2.0],
     [-1.5, 2.7, 3.3, -0.8]]

class Layer_Dense:
    def __init__(self,n_inputs,n_neurons):
        self.weights = 0.10 * np.random.randn(n_inputs,n_neurons)
        self.bias = np.zeros((1,n_neurons))
    
    def forward(self,input):
        self.output = np.dot(input,self.weights) + self.bias

Layer1 = Layer_Dense(4,5)
Layer2 = Layer_Dense(5,2)

Layer1.forward(X)
Layer2.forward(Layer1.output)

print(Layer2.output)