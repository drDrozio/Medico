# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 13:12:58 2020

@author: Armaan
"""

import pandas as pd
import numpy as np
#loading the dataset
dataset=pd.read_csv('C:\\Users\\Armaan\\Desktop\\SOFTWARE PROJECT\\Breast_cancer_data.csv')
#dividing x and y into independent and dependent parts
x=dataset.iloc[:,:5]
y=dataset.iloc[:,-1]
#checking null values in a dataset
print(dataset.isnull().sum())
#dividing the dataset into training set and test set
from  sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=1)

#applying logistic regression'
from sklearn.linear_model import LogisticRegression
model=LogisticRegression(random_state=0)
model.fit(x_train,y_train)


#predicting test set results
y_pred=np.where(model.predict_proba(x_test)[:,1]>0.167,1,0)


#confusion matrix
from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,y_pred)