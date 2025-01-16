### Assignment 6: Linear Algebra
import numpy as np;

# 1. Create a NumPy array of shape (3, 3) representing a matrix. 
# Compute its determinant, inverse, and eigenvalues.

arr1 = np.random.randint(1, 10, size=(3, 3))
deterninant = np.linalg.det(arr1)
print(deterninant)
inverse = np.linalg.inv(arr1)
print(inverse)
eigenValues = np.linalg.eigvals(arr1)
print(inverse)
# 2. Create two NumPy arrays of shape (2, 3) and (3, 2). 
# Perform matrix multiplication on these arrays.

arr2 = np.random.randint(1, 10, size=(2, 3))
arr3 = np.random.randint(1, 10, size=(3, 2))
result = np.dot(arr2, arr3)
print(arr2)
print(arr3)
print(result)
