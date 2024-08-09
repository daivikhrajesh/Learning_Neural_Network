# Neural Network with ReLU and Softmax Activation

This project demonstrates the implementation of a simple neural network in Python using NumPy. The network consists of two dense layers, with ReLU activation after the first layer and Softmax activation after the second layer. The network is trained on the spiral dataset, a common dataset used for visualizing classification problems.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Example Output](#example-output)

## Introduction

The code in this repository implements a basic feedforward neural network with the following structure:

1. **First Dense Layer**: Takes input data and applies a linear transformation.
2. **ReLU Activation**: Applies the ReLU (Rectified Linear Unit) activation function to introduce non-linearity.
3. **Second Dense Layer**: Another linear transformation is applied.
4. **Softmax Activation**: Converts the output into a probability distribution over three classes.

This simple neural network is trained on a synthetic spiral dataset, which is commonly used to test the performance of classification algorithms.

## Installation

To run this code, you'll need Python 3.x installed on your machine. Additionally, you'll need to install the following Python packages:

- `numpy`
- `nnfs`

You can install the required packages using pip:

```bash
pip install numpy nnfs
```

The `nnfs` library includes helper functions and datasets specifically designed for learning neural networks.

### Example Output

Here is an example of the output you might see after running the script:

```
[[0.33333333 0.33333333 0.33333333]
 [0.33333333 0.33333333 0.33333333]
 [0.33333333 0.33333333 0.33333333]
 [0.33333333 0.33333333 0.33333333]
 [0.33333333 0.33333333 0.33333333]]
```

This output shows the probability distribution across the three classes for the first five samples. Since the network has not been trained, the initial outputs are roughly uniform distributions.
