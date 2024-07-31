import sys
import numpy as np
import matplotlib as mlt

input = [1,2,3,2.5]
weights1 = [.2,.8,-.5,1.0]
weights2 = [.5,-0.91,0.26,-0.5]
weights3 = [-.26,-.27,.17,.87]


bias1 = 2
bias2 = 3
bias3 = .5

output1,output2,output3 = 0,0,0

for i,j in zip(input,weights1):
    output1+= i*j
for i,j in zip(input,weights2):
    output2+=i*j
for i,j in zip(input,weights3):
    output3+= i*j

output1+=bias1
output2+=bias2
output3+=bias3
print([output1,output2,output3])