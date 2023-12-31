# -*- coding: utf-8 -*-
"""logistic regression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cxGAxQdAlkpdUlpEwaxo0qBnFfVqEbob
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
data=pd.read_csv('/content/heart.csv')
#define target variables and features
y=data['output']
X=data.drop('output',axis=1)
#split the data into training and testing data sets
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
#to run the code multiple times with the same random state, need to get the same split each time so random_state=42
scaler=StandardScaler()
scale=scaler.fit(X_train)
X_train=scale.transform(X_train)
X_test=scale.transform(X_test)
#creating logistic regression model
model=LogisticRegression()
#train the model
model.fit(X_train,y_train)
#make predictions on test data
pred=model.predict(X_test)
res=pd.DataFrame({'Actual': y_test,'Predicted':pred})
print(res)
# Evaluate the model
from sklearn import metrics
# Accuracy
accuracy = metrics.accuracy_score(y_test,pred)
print("Accuracy:", accuracy)
# Precision, Recall, and F1-Score for each class
precision, recall, f1_score, support = metrics.precision_recall_fscore_support(y_test,pred,labels=model.classes_)
for i, class_label in enumerate(model.classes_):
    print(f"Class {class_label}:")
    print(f"  Precision: {precision[i]}")
    print(f"  Recall: {recall[i]}")
    print(f"  F1-Score: {f1_score[i]}")
    print(f"  Support: {support[i]}\n")
# Confusion Matrix
confusion_matrix = metrics.confusion_matrix(y_test, pred)
print("Confusion Matrix:")
print(confusion_matrix)

# Plot a heatmap of the confusion matrix
plt.figure(figsize=(4, 4))
sns.heatmap(confusion_matrix, annot=True, fmt="d", cmap="inferno", xticklabels=model.classes_, yticklabels=model.classes_)
plt.xlabel("Predicted")
plt.ylabel("True")
plt.title("Confusion Matrix")
plt.show()

res=pd.DataFrame({'Actual': y_test,'Predicted':pred})
res