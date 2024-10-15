import pandas as pd
import numpy as np 
db=pd.DataFrame(np.random.rand(56,12),index=np.arange(56))
# s=db.head()
# print(s)
# n=db[0][0]=50.0
# db.sort_index(axis=0,ascending=False)
# x=db.index
# x=db.columns
# x=db.to_numpy()
# print(x)
# print(x)
# print(db)
db2=db.copy()
db2[0][0]=786.786
print(db2.head(5))
# print(db.head(5))
num =db2[0][1] #column and  row
print(num) 