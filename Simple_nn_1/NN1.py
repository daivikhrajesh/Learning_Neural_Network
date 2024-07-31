import sys
import numpy as np
import matplotlib as mlt

input = [1.2,3.2,3.4]
weights = [4.5,6.5,9.6]
bias = 3

""" output = input[0]*weights[0]+input[1]*weights[1]+input[2]*weights[2]+bias
print(output) """

output1 = 0

for i,j in zip(input,weights):
    output1+= i*j

output1+=bias
print(output1)