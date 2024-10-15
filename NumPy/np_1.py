import numpy as np
arr=np.array([1,2,2,3]) # 1D array
arr2=np.array([[1,2,23],[23,56,89]]) # 2D array
print("one demensional array->",arr)
# print(type(arr))
print("two demensional array->",arr2)
print(arr2[0,1])
#First attribute for representing the columan and second for row
arr2[0,1]=30
arr2[1,2]=786
print(arr2)
print(arr2.shape) # To print the  row and column of array
print(arr2.dtype) # To check the d type for array