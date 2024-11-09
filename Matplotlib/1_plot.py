import matplotlib.pyplot as plt
import numpy as np
a=["orange","apple","Watermelon","litchi","annanas"]
b=[3,6,6,5,4,5]
c=[5,2,1,2,5,8]
arr=np.arange(len(a))
# add color in graph
col=["r","g","b","y","r"]
plt.bar(a,arr,color=col,width=1)
plt.bar(c,b,color="black",width=1,label="hrllo")
plt.title("Price of fruits")
plt.xlabel("fruits",fontsize=20)
plt.ylabel("price per kg")
plt.legend()
plt.show() 