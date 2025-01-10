import numpy as np;

### Assignment 3: Array Operations

# 1. Create two NumPy arrays of shape (3, 4) filled with random integers. 
# Perform element-wise addition, subtraction, multiplication, and division.

arr1 = np.random.randint(1, 100, size=(3, 4))
arr2 = np.random.randint(1, 100, size=(3, 4))

print(arr1 + arr2)
print(arr1 - arr2)
print(arr1 * arr2)
print(arr1 / arr2)

# 2. Create a NumPy array of shape (4, 4) with values from 1 to 16. 
# Compute the row-wise and column-wise sum.

arr = np.arange(1, 17).reshape(4, 4)
rowSum = np.sum(arr,  axis=1)
colSum = np.sum(arr,  axis=0)
print(arr, 'arr', rowSum, 'rowSum', colSum, 'colSum')