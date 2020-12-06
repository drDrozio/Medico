# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#importing libraries
import numpy as np
from numpy import nan
import pandas as pd
import matplotlib.pyplot as plt

#importing dataset
dataset=pd.read_csv('C:\\Users\\Armaan\\Desktop\\SOFTWARE PROJECT\\datasets_2607_4342_indian_liver_patient.csv')
x=pd.DataFrame(dataset.iloc[:,:-1].values)
y=dataset.iloc[:,10].values


#importical data or genders(0,1)
from sklearn.preprocessing import LabelEncoder
labelencoder_x=LabelEncoder()
x[1]=labelencoder_x.fit_transform(x[1])

#filling missing values in 9th coloumn
x.fillna(x.mean(),inplace=True)

#dividing dataset into training set and test set
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)

#apply naive bayes model
from sklearn.naive_bayes import GaussianNB
model=GaussianNB()
model.fit(x_train,y_train)

#predicting test set results

y_pred=model.predict(x_test)

#confusion matrix
from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,y_pred)


