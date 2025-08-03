from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv("data.csv")
# print(data)
x=data[['YearsExperience']]
y=data['Salary']
plt.scatter(x,y)
plt.show()

xtrain,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

model=LinearRegression()
model.fit(xtrain,y_train)
score=model.score(x_test,y_test)*100

print(model.predict([[10]]),score)