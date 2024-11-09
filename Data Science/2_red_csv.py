import pandas as pd
data=pd.read_csv('bus.csv')
show=data.head(5)
show_tail=data.tail(10)
# print(show,show_tail)
# print(data.shape)
# print(data.info())
# print(data.describe())
# print(data.isnull().sum())
