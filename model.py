import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle
from sklearn.metrics import confusion_matrix,classification_report,accuracy_score
#"train",'mysql://root:''@localhost:3307/test'
titanic_data = pd.read_sql("titanic",'mysql://root:''@localhost:3307/test')
print(titanic_data.head(5))
print(titanic_data['Age'].head(10))
titanic_data['Age'].fillna(titanic_data['Age'].mean(),inplace=True)
print(titanic_data['Age'].isna().sum())
gender= pd.get_dummies(titanic_data['Sex'],drop_first=True)
titanic_data['Gender']=gender
titanic_data.drop(['PassengerId','Name','Sex','Ticket','Cabin','Fare','Embarked'],axis=1,inplace=True)
print(titanic_data.columns)
df=titanic_data
df.to_csv("cleaned.csv",columns=['Gender','Age','Pclass','Parch','SibSp'])
x = titanic_data[['Pclass','Age','SibSp','Parch','Gender']]
y = titanic_data['Survived']
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.20,random_state=42)
lr= LogisticRegression()
fit=lr.fit(x_train,y_train)
predict = lr.predict(x_test)
score = accuracy_score(y_test,predict)
print(score*100)
f=open('titanic.pkl','wb')
pickle.dump(fit,f)
