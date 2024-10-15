import numpy as np
arr=np.array([1,2,3])
print(arr )

arr2=np.array({1,2,3,4,4,5,3,2,2,4}) 
print(arr2) #because now it is a set array so it eliminate the duplicates

arr3=np.zeros((3,5)) #give three row and 5 column of zero to array
print (arr3)

# so further more
arr4=np.arange(26)
print(arr4)
# print(arr4[3])
arr5=np.linspace(1,20,5)
#this mean build an array from 1 to twenty and give me 5 array with same difference
print(arr5)
#empty array fill with random numbers 
arr6=np.empty((4,6))
print(arr6)

arr_2d=np.array([[1,2,3],[2,3,4]])
print(arr_2d.shape)
print(arr_2d)

arr7=np.arange(99) # for arranging to specific number to array 
print(arr7)
print(arr7.reshape(3,33)) 
# point to be noted the reshpae attribute should be  = to total array numbr if of multiple firt element to seconf element  for example 3 into 33 is eaqal to 99 so its is true  otherwise you will get error

arr_ravel=arr7.ravel() # To re-arrange the array like first
print(arr_ravel)