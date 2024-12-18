### Assignment 8: Fancy Indexing and Boolean Indexing
import numpy as np;

# 1. Create a NumPy array of shape (5, 5) filled with random integers. 
# Use fancy indexing to extract the elements at the corners of the array.
arr1 = np.random.randint(1, 10, size = (5, 5))
corners  = arr1[[0, 0, -1, -1], [0, -1, 0, -1]]
print(arr1, 'arr1')
print(corners, 'corners')
# 2. Create a NumPy array of shape (4, 4) filled with random integers. 
# Use boolean indexing to set all elements greater than 10 to 10.
arr2 = np.random.randint(1, 20, size=(4, 4))
print(arr2)
arr2[arr2 > 10] = 10
print(arr2)