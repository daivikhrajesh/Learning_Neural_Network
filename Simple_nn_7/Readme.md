# Softmax Cross-Entropy Loss Example

This repository contains a simple Python script that calculates the cross-entropy loss for a single instance using the output of a softmax function and the corresponding target output.

## Overview

Cross-entropy loss is commonly used as a loss function in classification problems, especially in combination with softmax activation in neural networks. This example demonstrates how to compute the loss for a specific prediction.

### Softmax Output

In this example, the softmax output is a list of probabilities for each class:

```python
softmax_output = [0.7, 0.1, 0.2]
```

This indicates that the model is 70% confident in the first class, 10% in the second, and 20% in the third.

### Target Output

The target output is a one-hot encoded vector indicating the correct class:

```python
target_output = [1, 0, 0]
```

Here, the correct class is the first one.

### Cross-Entropy Loss Calculation

The cross-entropy loss is computed using the following formula:

```python
loss = -(math.log(softmax_output[0]) * target_output[0] +
         math.log(softmax_output[1]) * target_output[1] +
         math.log(softmax_output[2]) * target_output[2])
```

This formula sums the negative log probabilities of the predicted classes, weighted by the target output. Since the target is `[1, 0, 0]`, only the first term contributes to the loss:

```python
loss = -math.log(0.7)
```

### Output

The script prints the computed loss and compares it with the log loss of other example probabilities:

```python
print(loss)
print(-math.log(0.7))
print(-math.log(0.5))
```

### Example Output

Running the script will produce the following output:

```
0.35667494393873245
0.35667494393873245
0.6931471805599453
```

This shows the calculated loss for the correct prediction (0.7 probability) and compares it with another example (0.5 probability).
