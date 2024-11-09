import matplotlib.pyplot as mt
a=[10,20,30,40,50]
b=[5,6,7,4,5]
siz=[20,30,25,76,8]
col=[25,14,50,66,3]
mt.scatter(a,b,c=col,s=siz)
mt.title("Just Random",fontsize=20,color='r')
mt.colorbar()

mt.show()