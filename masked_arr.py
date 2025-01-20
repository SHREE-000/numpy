### Assignment 10: Masked Arrays
import numpy as np;
import numpy.ma as ma;

# 1. Create a masked array of shape (4, 4) 
# with random integers and mask the elements greater than 10. 
# Compute the sum of the unmasked elements.
arr1 = np.random.randint(5, 15, size=(4, 4))
maskedArr = ma.masked_greater(arr1, 10)
sum = maskedArr.sum()
print(arr1, 'arr1')
print(maskedArr, 'maskedArr', sum, "sum")
# 2. Create a masked array of shape (3, 3) 
# with random integers and mask the diagonal elements. 
# Replace the masked elements with the mean of the unmasked elements.
array = np.random.randint(1, 21, size=(3, 3))
masked_array = ma.masked_array(array, mask=np.eye(3, dtype=bool))
print(array, 'array')
print(masked_array, 'masked_array')
mean_un_masked = masked_array.mean()
filled_masked_arr = masked_array.fill(mean_un_masked)