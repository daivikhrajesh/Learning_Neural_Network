# Simple_Neural_Network

## Overview

This script performs a simple linear transformation operation. It calculates a weighted sum of inputs, adds a bias term, and prints the result. The script uses basic Python functionalities without external dependencies, although it imports libraries that are not utilized in the current version.

## Script Description

The script performs the following operations:

1. **Initialization**:

   - `input`: A list of input values.
   - `weights`: A list of weights corresponding to the input values.
   - `bias`: A bias term to be added to the weighted sum.

2. **Calculation**:

   - The script calculates the weighted sum of the inputs and adds the bias term.
   - It iterates through pairs of input values and weights, computes their product, accumulates these products, and then adds the bias.

3. **Output**:
   - The final result is printed to the console.

## How It Works

1. **Input and Weights**:

   - `input` and `weights` are lists containing numerical values.
   - These lists are assumed to be of the same length.

2. **Dot Product Calculation**:

   - The script calculates the dot product of `input` and `weights` using a `for` loop and accumulates the result in the `output1` variable.

3. **Adding Bias**:

   - After calculating the dot product, the `bias` is added to the accumulated result.

4. **Print Result**:
   - The final result, which is the weighted sum plus the bias, is printed.

## Notes

- Make sure that the length of `input` and `weights` lists are the same; otherwise, `zip` will truncate the longer list to match the length of the shorter one.
- Modify the `input`, `weights`, and `bias` variables to suit your specific needs for different calculations.
