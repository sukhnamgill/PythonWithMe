list_1=[1,2,3,4,5,6,7,8,9,10]
list_2=[i for i in list_1 if i%2==0]
list_3=[i for i in list_1 if i%2==1]
print("Even",list_2)
print("odd",list_3)