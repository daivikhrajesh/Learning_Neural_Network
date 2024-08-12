import math 
import numpy as np
import nnfs

nnfs.init()


layer = [4.8, 1.21, 2.385]

E= math.e

""" exp = []

for output in layer:
    exp.append(E**output) """

exp = np.exp(layer)

print(exp)

""" norm_base = sum(exp)

norm_val = []

for val in exp:
    norm_val.append(val/norm_base) """

norm_val = exp / np.sum(exp)

print(norm_val)
print(sum(norm_val))

layer_op = [[4.8, 1.21, 2.385],
            [8.9,-1.81,0.2],
            [1.41,1.051, 0.026]]

exp_val = np.exp(layer_op)

# axis= 0 ---> Column and axis= 1 ---> row 
# keepdims= True ---> returns the array od matrix in tthe same exact shape wanted as a **Transpose of the matrix**

#print(np.sum(layer_op, axis=1, keepdims=True))

norm_val_ = exp_val/np.sum(layer_op, axis=1, keepdims=True)

print(norm_val_)