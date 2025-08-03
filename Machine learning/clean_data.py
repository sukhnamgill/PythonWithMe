import numpy as np
arr=np.array([[1,2,3,4,10,11,12,13,4 ,5,6,7]])
# for reshaping the array

arr.reshape(1,12)
# print(type(arr)) # to know the type of thr array
arr_2=np.array([(1,2,3),(4,5,6)]) 

arr4=np.zeros([1,2],dtype=int)
# print(arr4)/

arr5=np.ones([5,3],dtype=float) 
# print(arr5)

string_arr=np.array(['sukhnam','23'])
# print(string_arr)
# print(type(string_arr))
f_e=(string_arr[1])
print(type(f_e))
f_e=int(f_e)
print(type(f_e))
