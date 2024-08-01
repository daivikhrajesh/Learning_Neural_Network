# README

## Overview
This project implements a simple neural network with two dense layers, designed to perform a forward pass using randomly generated weights and biases. The network processes an input dataset `X` through these layers, resulting in an output after the second layer.

## Structure
The project contains the following components:
1. **Input Data (`X`)**: A list of input samples, each with 4 features.
2. **Layer_Dense Class**: A class that defines a dense layer with methods to initialize weights and biases, and to perform a forward pass.
3. **Network Initialization**: Creation of two dense layers with specified input and output sizes.
4. **Forward Pass**: Passing the input data through the layers to get the final output.

**Output**:
   The script will output the result of the forward pass of the second layer.

### Layer_Dense Class

- **`__init__` Method**: Initializes the layer with random weights and zero biases. The weights are scaled by 0.10.
- **`forward` Method**: Computes the dot product of the input and weights, then adds the bias.

- The input data `X` is passed through `Layer1` and then the output of `Layer1` is passed through `Layer2`.
- The final output after `Layer2` is printed.

## Example Output
The output will be a 3x2 matrix (since `Layer2` has 2 neurons and there are 3 input samples), which might look something like:
```
[[-0.0346103   0.00466297]
 [-0.07731586  0.0147267 ]
 [-0.00743155 -0.00069655]]
```