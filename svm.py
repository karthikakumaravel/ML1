# -*- coding: utf-8 -*-
"""SVM.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aYOodbkio4uzrOmbZwSkLRNynh7mkda-
"""

from sklearn.model_selection import train_test_split
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from sklearn.svm import SVC
from sklearn import svm
import numpy as np

titanic=pd.read_csv("https://raw.githubusercontent.com/ezioauditore-tech/AI/main/datasets/Titanic/train.csv")
titanic

titanic.drop(['PassengerId','Name','Ticket'],axis=1,inplace=True)
titanic.head()

titanic.info()

titanic.isnull().sum()

#titanic[titanic.Embarked.isnull()]
print(titanic[titanic.Embarked.isnull()])

titanic.drop(['Cabin'],axis=1,inplace=True)
titanic["Age"]=titanic["Age"].fillna(titanic["Age"].median())
titanic["Embarked"]=titanic["Embarked"].fillna("C")
titanic.Sex=titanic.Sex.replace(['male','female'],[0,1])
titanic.Embarked=titanic.Embarked.replace(['S','C','Q'],[0,1,2])

titanic.dropna(inplace=True)
titanic

titanic1=pd.read_csv("https://raw.githubusercontent.com/ezioauditore-tech/AI/main/datasets/Titanic/test.csv")
titanic1

titanic1.drop(['PassengerId','Name','Ticket'],axis=1,inplace=True)
titanic.head()

titanic1.info()

titanic1.isnull().sum()

print(titanic1[titanic1.Embarked.isnull()])

titanic1.drop(['Cabin'],axis=1,inplace=True)
titanic1["Age"]=titanic1["Age"].fillna(titanic1["Age"].median())
titanic1["Embarked"]=titanic1["Embarked"].fillna("C")
titanic1.Sex=titanic1.Sex.replace(['male','female'],[0,1])
titanic1.Embarked=titanic1.Embarked.replace(['S','C','Q'],[0,1,2])

titanic1.dropna(inplace=True)
titanic1

features=["Pclass","Sex","Age","SibSp","Parch","Fare","Embarked"]

C=0.7
clf=svm.SVC(kernel='linear',C=C).fit(titanic[features],titanic["Survived"])

prediction=clf.predict(titanic1[features])
titanic1