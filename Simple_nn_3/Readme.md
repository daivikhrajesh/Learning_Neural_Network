# Neural Network Layer Output Calculation

This project demonstrates a simple calculation of the output of a neural network layer using both a manual loop-based approach and a more efficient approach using NumPy's `dot` function.

## Code Explanation

### Inputs

1. **Input Values:**

   ```python
   input = [1, 2, 3, 2.5]
   ```

   These are the inputs to the neural network layer.

2. **Weights:**

   ```python
   weights1 = [0.2, 0.8, -0.5, 1.0]
   weights2 = [0.5, -0.91, 0.26, -0.5]
   weights3 = [-0.26, -0.27, 0.17, 0.87]
   ```

   These are the weights for each neuron in the layer. Each list represents the weights for one neuron.

3. **Biases:**

   ```python
   bias1 = 2
   bias2 = 3
   bias3 = 0.5
   ```

   These are the biases for each neuron in the layer.

### Manual Loop-Based Calculation

This section of the code manually calculates the output of each neuron by iterating over the inputs and weights, multiplying them, summing the results, and adding the bias:

```python
layer_output = []
for n_weights, n_bias in zip(weights, bias):
    neuron_output = 0
    for x, y in zip(input, n_weights):
        neuron_output += x * y
    neuron_output += n_bias
    layer_output.append(neuron_output)

print(layer_output)
```

### Efficient Calculation Using NumPy

This section of the code uses NumPy to perform the same calculation more efficiently:

```python
output = np.dot(weights, input) + bias
print(output)
```

## Explanation

- The manual loop-based approach iterates over each neuron's weights and inputs, multiplies them together, sums the results, and adds the bias.
- The NumPy approach leverages the `dot` function to perform the same operation in a more concise and efficient manner.

This example shows how you can implement basic neural network layer calculations and how NumPy can simplify and speed up your computations.
