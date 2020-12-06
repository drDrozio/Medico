# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 00:01:01 2020

@author: Armaan
"""
#importing libraries 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#importing datset
dataset=pd.read_csv('C:\\Users\\Armaan\\Desktop\\SOFTWARE PROJECT\\cardio_train.csv',sep=';')
x=pd.DataFrame(dataset.iloc[:,:-1].values)
y=dataset.iloc[:,12].values

#checked no null entry in any column
#print(dataset.isnull().sum())

#dividing training ,test set
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)


#training dataset by applying suitable model
from sklearn.linear_model import LogisticRegression
model= LogisticRegression(random_state=0)
model.fit(x_train,y_train)


#predicting results
y_pred_thr3=np.where(model.predict_proba(x_test)[:,1]>0.004,1,0)

#confusion matrix
from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,y_pred_thr3)