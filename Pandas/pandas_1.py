import pandas as pd
import numpy as np
dic={"names":["sukhnam","Mayank","Nitin","Gurkirat"],
     "age":[19,18,19,18],
     "village":["badhni","ludhiana","ludhiana","Dehraka"]
}
# dic2={"name":'sukhnam','age':19
     
s=pd.DataFrame(dic)
# s.to_csv("ex.csv")
# if you wnat that index not come then use index=False
# s.to_csv('new.csv',index=False)
print(s)