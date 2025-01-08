import numpy as np

# Create a NumPy array of shape (5, 5) filled with random integers between 1 and 20. 
# Replace all the elements in the third column with 1.

arr = np.random.randint(1, 21, size=(5, 5))
arr[:, 2] = [1, 1, 1, 1, 1]
print(arr)

# 2. Create a NumPy array of shape (4, 4) with values from 1 to 16. 
# Replace the diagonal elements with 0.

npArr = np.arange(1, 17).reshape(4, 4)
np.fill_diagonal(npArr, 0)
print(npArr)