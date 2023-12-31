# -*- coding: utf-8 -*-
"""NB.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NvFjq_0KjOM_pP0I0jGuL7GvoEXiptjC
"""

import pandas as pd
import numpy as np
from sklearn.naive_bayes import GaussianNB

dataframe=pd.read_csv('https://raw.githubusercontent.com/ezioauditore-tech/AI/main/datasets/Titanic/train.csv')
test_dataframe=pd.read_csv('https://raw.githubusercontent.com/ezioauditore-tech/AI/main/datasets/Titanic/test.csv')
passangerId=test_dataframe["PassengerId"]

final_dataframe=dataframe[['Survived','Pclass','Sex','Age','SibSp','Fare','Embarked']]
final_dataframe=final_dataframe.dropna()
final_dataframe.head()

final_dataframe["Sex"]=final_dataframe["Sex"].replace(to_replace=final_dataframe["Sex"].unique(),value=[1,0])

final_dataframe=pd.get_dummies(final_dataframe,drop_first=True)#categorical values

train_y=final_dataframe["Survived"]
train_x=final_dataframe[['Pclass','Sex','Age','SibSp','Fare','Embarked_Q','Embarked_S']]

from sklearn.model_selection import train_test_split
train_data,val_data,train_target,val_target=train_test_split(train_x,train_y,train_size=0.8)

model=GaussianNB()
model.fit(train_data,train_target)
val_pred=model.predict(val_data)

from sklearn.metrics import accuracy_score
print('model accuracy score :(0:0.4f)',format(accuracy_score(val_target,val_pred)*100)+"%")

