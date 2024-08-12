# Neural Network from Scratch in Python

This repository contains a simple implementation of a neural network built from scratch using Python and NumPy. The goal is to demonstrate the basic concepts of neural networks, including layers, activation functions, and loss calculations, without relying on high-level machine learning libraries.

## Table of Contents

- [Project Structure](#project-structure)
- [Explanation of the Code](#explanation-of-the-code)
  - [Layer_Dense Class](#layer_dense-class)
  - [Activation Functions](#activation-functions)
  - [Loss Functions](#loss-functions)
- [Example Output](#example-output)
- [Acknowledgments](#acknowledgments)


## Explanation of the Code

### Layer_Dense Class

The `Layer_Dense` class represents a fully connected layer in the neural network. It initializes the layer with random weights and biases, and computes the output based on the input:

```python
class Layer_Dense:
    def __init__(self, n_inputs, n_neurons):
        self.weights = 0.1 * np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))
        
    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases
```

### Activation Functions

The code implements two activation functions:

- **ReLU (Rectified Linear Unit)**: 
  ```python
  class Activation_ReLU:
      def forward(self, inputs):
          self.output = np.maximum(0, inputs)
  ```

- **Softmax**: 
  ```python
  class Activation_Softmax:
      def forward(self, inputs):
          exp_values = np.exp(inputs - np.max(inputs, axis=1, keepdims=True))
          probabilities = exp_values / np.sum(exp_values, axis=1, keepdims=True)
          self.output = probabilities
  ```

### Loss Functions

The `Loss_CategoricalCrossentropy` class calculates the loss using categorical crossentropy:

```python
class Loss_CategoricalCrossentropy(Loss):
    def forward(self, y_pred, y_true):
        samples = len(y_pred)
        y_pred_clipped = np.clip(y_pred, 1e-7, 1-1e-7)

        if len(y_true.shape) == 1:
            correct_confidences = y_pred_clipped[range(samples), y_true]
        elif len(y_true.shape) == 2:
            correct_confidences = np.sum(y_pred_clipped*y_true, axis=1)

        negative_log_likelihood = -np.log(correct_confidences)
        return negative_log_likelihood
```

### Example Output

After running the script, you will see the output of the softmax activation and the loss calculated for the spiral data:

```python
print(activation2.output[:5])
print(loss)
```

This will display the first five predictions made by the network and the overall loss.