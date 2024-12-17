import numpy as np;

arr = [2, 4, 2, 1]
changed_arr = np.array(arr)
result = changed_arr.reshape(2, 2)
# print(result)

arr1 = np.array([[2, 5, 2], [2, 6, 8], [5, 1, 6]])
print(arr1[1:2, 2:])