import numpy as np;

### Assignment 2: Array Indexing and Slicing

# 1. Create a NumPy array of shape (6, 6) with values from 1 to 36. 
# Extract the sub-array consisting of the 3rd to 5th rows and 2nd to 4th columns.

arr = np.random.randint(1, 37, size=(6, 6))
print(arr[2:5, 1: 4])

# 2. Create a NumPy array of shape (5, 5) with random integers. 
# Extract the elements on the border.

npArr = np.random.randint(1, 100, size=(5, 5))
borderElem = np.concatenate((npArr[0, :], npArr[1:-1, 0], npArr[-1, :], npArr[1:-1, -1]))
print(borderElem)