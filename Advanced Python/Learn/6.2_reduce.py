from functools import reduce
print("iam reduce function")
l=[1,2,3,4,5,6,7,8,9,10]
lamb=lambda x,y:y+x
se=(reduce(lamb,[41,12,2,21,12,5]))
print(se)