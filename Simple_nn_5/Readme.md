# README

## Overview
This project demonstrates a basic implementation of a neural network with one dense layer and a ReLU activation function. The network processes an input dataset `X`, which is generated using the `spiral_data` function from the `nnfs` library.

## Structure
The project consists of the following components:
1. **Input Data (`X`, `y`)**: Generated using the `spiral_data` function, which provides a set of input samples and corresponding labels.
2. **Layer_Dense Class**: Defines a dense (fully connected) layer, initializing weights and biases, and performing the forward pass.
3. **ReLU Class**: Implements the ReLU activation function, applying it to the output of the dense layer.
4. **Network Initialization and Execution**: Initialization of the dense layer and activation function, followed by execution of the forward pass through these components.

**Output**:
   The script will output the result of the forward pass after applying the ReLU activation function.

## Code Explanation

### Input Data
```python
X, y = spiral_data(100, 3)
```
Generate spiral data with 100 samples per class and 3 classes, resulting in `X` (input features) and `y` (labels).

### Layer_Dense Class
```python
class Layer_Dense:
    def __init__(self, n_inputs, n_neurons):
        self.weights = 0.10 * np.random.randn(n_inputs, n_neurons)
        self.bias = np.zeros((1, n_neurons))
    
    def forward(self, input):
        self.output = np.dot(input, self.weights) + self.bias
```
- **`__init__` Method**: Initializes the layer with random weights and zero biases. Weights are scaled by 0.10.
- **`forward` Method**: Computes the dot product of the input and weights, then adds the bias.

### ReLU Class
```python
class ReLU:
    def forward(self, input):
        self.output = np.maximum(0, input)
```
- **`forward` Method**: Applies the ReLU activation function, setting all negative values to zero.

### Network Initialization and Execution
```python
Layer1 = Layer_Dense(2, 5)
activation1 = ReLU()

Layer1.forward(X)
activation1.forward(Layer1.output)
print(activation1.output)
```
- `Layer1` is initialized with 2 input features and 5 neurons.
- `activation1` is an instance of the ReLU activation function.
- The input data `X` is passed through `Layer1`, and the output is then passed through `activation1`.
- The final output after the ReLU activation is printed.