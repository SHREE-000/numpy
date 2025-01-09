### Assignment 7: Advanced Array Manipulation
import numpy as np;

# 1. Create a NumPy array of shape (3, 3) with values from 1 to 9. 
# Reshape the array to shape (1, 9) and then to shape (9, 1).
arr1 = np.arange(1, 10).reshape(3, 3)
arr2 = np.reshape(arr1, (1, 9))
arr3 = np.reshape(arr2, (9, 1))
print(arr1)
print(arr2)
print(arr3)
# 2. Create a NumPy array of shape (5, 5) filled with random integers. 
# Flatten the array and then reshape it back to (5, 5). 
arr4 = np.random.randint(1, 10, size=(5, 5))
arr5 = arr4.flatten()
arr6 = arr5.reshape(5, 5)
print(arr4)
print(arr5)
print(arr6)