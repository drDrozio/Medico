import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
import pickle as pkl
import joblib
# age        float64
# sex        float64
# cp         float64
# restbp     float64
# chol       float64
# fbs        float64
# restecg    float64
# thalach    float64
# exang      float64
# oldpeak    float64
# slope      float64
# ca          object
# thal        object
# hd           int64  Y value

class heart_disease_ml():
	def preprocess(dic):
		x = {}
		x['age'] = dic['age']
		x['sex'] = dic['sex']
		x['cp'] = dic['cp']
		x['restbp'] = dic['restbp']
		x['chol'] = dic['chol']
		x['fbs'] = dic['fbs']
		x['restecg'] = dic['restecg']
		x['thalach'] = dic['thalach']
		x['exang'] = dic['exang']
		x['oldpeak'] = dic['oldpeak']
		x['slope'] = dic['slope']
		x['ca'] = dic['ca']
		x['thal'] = dic['thal']
		X=pd.DataFrame({'x':x}).transpose()
		return X

	def predict_disease(X):
		model = joblib.load('ml_models/heart_disease3.pkl')
		pred = model.predict(X)[0]
		return pred



