### Assignment 9: Structured Arrays
import numpy as np;

# 1. Create a structured array with fields 'name' (string), 'age' (integer), and 'weight' (float). 
# Add some data and sort the array by age.
datatype = [("name", "U10"), ("age", "i4"), ("weight", "f4")]
arr1 = np.array([("Shree", "28", "72.02"), ("Paru", "24", "68.5")], dtype=datatype)
sortedArr = np.sort(arr1, order = "age")
print(arr1, 'arr1', sortedArr, 'sortedArr')
# 2. Create a structured array with fields 'x' and 'y' (both integers). 
# Add some data and compute the Euclidean distance between each pair of points.
datatype1 = [("x", "i4"), ("y", "i4")]
data = np.array([(10, 20), (4, 5)], dtype=datatype1)
distances = np.sqrt((data['x'][:, np.newaxis] - data['x'])**2 + (data['y'][:, np.newaxis] - data['y'])**2)
print("Euclidean distances:")
print(distances)