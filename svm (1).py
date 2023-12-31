# -*- coding: utf-8 -*-
"""SVM.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jtSLljbaVOfs-fvL9lrGry89Vl2UbJx_
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

from sklearn.svm import SVC
from sklearn import svm

data=pd.read_csv('/content/heart (1).csv')
data.head()

y=data['output']
X=data.drop('output',axis=1)
print(X.head())
print(y)

train_y=data["output"]
train_x=data[['age','sex','cp','trtbps','chol','fbs','restecg','exng','oldpeak','slp','caa','thall']]

from sklearn.model_selection import train_test_split
train_data,val_data,train_target,val_target=train_test_split(train_x,train_y,train_size=0.8)

C=0.7
clf=svm.SVC(kernel='linear',C=C).fit(train_data,train_target)
print(clf)

prediction=clf.predict(val_data)

res=pd.DataFrame({'Actual': val_target,'Predicted':prediction})
print(res)

print('model accuracy score :(0:0.4f)',format(accuracy_score(val_target,prediction)*100)+"%")

confusion_matrix(val_target,prediction)

tn,fp,fn,tp=confusion_matrix(val_target,prediction).ravel()
(tn,fp,fn,tp)

matrix=classification_report(val_target,prediction)
print('classification report:\n',matrix)

# Evaluate the model
from sklearn import metrics

# Accuracy
accuracy = metrics.accuracy_score(val_target,prediction)
print("Accuracy:", accuracy)

# Precision, Recall, and F1-Score for each class
precision, recall, f1_score, support = metrics.precision_recall_fscore_support(val_target,prediction,labels=clf.classes_)
for i, class_label in enumerate(clf.classes_):
    print(f"Class {class_label}:")
    print(f"  Precision: {precision[i]}")
    print(f"  Recall: {recall[i]}")
    print(f"  F1-Score: {f1_score[i]}")
    print(f"  Support: {support[i]}\n")

# Confusion Matrix
confusion_matrix = metrics.confusion_matrix(val_target, prediction)
print("Confusion Matrix:")
print(confusion_matrix)

# Plot a heatmap of the confusion matrix
plt.figure(figsize=(5, 5))
sns.heatmap(confusion_matrix, annot=True, fmt="d", cmap="inferno", xticklabels=clf.classes_, yticklabels=clf.classes_)
plt.xlabel("Predicted")
plt.ylabel("True")
plt.title("Confusion Matrix")
plt.show()