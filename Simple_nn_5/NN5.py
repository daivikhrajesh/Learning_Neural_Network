import random
import numpy as np
import nnfs
from nnfs.datasets import spiral_data


nnfs.init()

X = [[1, 2, 3, 2.5],
     [2.0, 5.0, -1.0, 2.0],
     [-1.5, 2.7, 3.3, -0.8]]

X,y = spiral_data(100,3)

class Layer_Dense:
    def __init__(self,n_inputs,n_neurons):
        self.weights = 0.10 * np.random.randn(n_inputs,n_neurons)
        self.bias = np.zeros((1,n_neurons))
    
    def forward(self,input):
        self.output = np.dot(input,self.weights) + self.bias

class ReLU:  #Rectified Linear Unit
    def forward(self,input):
        self.output = np.maximum(0,input)

Layer1 = Layer_Dense(2,5)
activation1 = ReLU()

Layer1.forward(X)
activation1.forward(Layer1.output)
print(activation1.output)