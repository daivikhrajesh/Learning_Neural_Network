# README

## Overview

This script performs a basic neural network layer computation. It calculates the outputs of three neurons in a neural network layer, each with its own set of weights and biases. The script uses simple list operations to compute the weighted sums of inputs, adds biases, and prints the final outputs for each neuron.

## Script Description

The script performs the following operations:

1. **Initialization**:

   - `input`: A list of input values.
   - `weights1`, `weights2`, `weights3`: Lists of weights for three neurons.
   - `bias1`, `bias2`, `bias3`: Bias values for the three neurons.

2. **Calculation**:

   - For each neuron, compute the dot product of the inputs and weights, and then add the corresponding bias.

3. **Output**:
   - Print the final computed outputs for the three neurons.

## How It Works

1. **Input and Weights**:

   - `input` is a list of input values that are fed into the neurons.
   - `weights1`, `weights2`, and `weights3` are lists containing the weights for each neuron.

2. **Dot Product Calculation**:

   - For each neuron, the dot product of the `input` list and the corresponding `weights` list is computed using a loop.

3. **Adding Bias**:

   - After computing the dot product for each neuron, the corresponding bias (`bias1`, `bias2`, `bias3`) is added to the result.

4. **Print Result**:
   - The final results for all three neurons are printed as a list.

## Notes

- Ensure that the length of the `input` list matches the length of each `weights` list; otherwise, the dot product calculation will be incorrect.
- Adjust the `input`, `weights`, and `bias` values as needed for different neural network configurations.
