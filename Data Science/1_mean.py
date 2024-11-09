import numpy as np
import pandas as pd
arr=np.array([5,45,1,2,8,9,36,25,21])
print(arr)
total=np.sum(arr)
sorted_d=arr.sort()
length=len(arr)
print(total/length)
print("printing mean by function of numpy",np.mean(arr))
print("wih pandas",arr.mean())
# print(arr)