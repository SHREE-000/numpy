import numpy as np;
### Assignment 5: Broadcasting

# 1. Create a NumPy array of shape (3, 3) filled with random integers. 
# Add a 1D array of shape (3,) to each row of the 2D array using broadcasting.

arr1 = np.random.randint(1, 10, size=(3, 3))
arr2 = np.random.randint(1, 10, size=(3, ))
arr = arr1 + arr2
print(arr, 'arr')

# 2. Create a NumPy array of shape (4, 4) filled with random integers. 
# Subtract a 1D array of shape (4,) from each column of the 2D array using broadcasting.
arr1 = np.random.randint(1, 10, size=(4, 4))
arr2 = np.random.randint(1, 10, size=(4, ))
arr = arr1 - arr2
print(arr)