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
		#Age
		x['age'] = np.float(dic['age'])
		#Sex
		x['sex'] = np.float(dic['sex'])
		#RestBP
		x['restbp'] = np.float(dic['restbp'])
		#Chol
		x['chol'] = np.float(dic['chol'])
		#FBS
		x['fbs'] = np.float(dic['fbs'])
		#Thalach
		x['thalach'] = np.float(dic['thalach'])
		#Exang
		x['exang'] = np.float(dic['exang'])
		#OldPeak
		x['oldpeak'] = np.float(dic['oldpeak'])
		#CA
		x['ca'] = dic['ca']
		#CP
		cp = np.float(dic['cp'])
		if cp == 1.0:
			x['cp_1.0'] = 1
			x['cp_2.0'] = 0
			x['cp_3.0'] = 0
			x['cp_4.0'] = 0
		elif cp == 4.0:
			x['cp_1.0'] = 0
			x['cp_2.0'] = 0
			x['cp_3.0'] = 0
			x['cp_4.0'] = 1
		elif cp == 3.0:
			x['cp_1.0'] = 0
			x['cp_2.0'] = 0
			x['cp_3.0'] = 1
			x['cp_4.0'] = 0
		else:
			x['cp_1.0'] = 0
			x['cp_2.0'] = 1
			x['cp_3.0'] = 0
			x['cp_4.0'] = 0

		#RestECG
		restecg = np.float(dic['restecg'])
		if restecg == 0.0:
			x['restecg_0.0'] = 1
			x['restecg_1.0'] = 0
			x['restecg_2.0'] = 0
		elif restecg == 1.0:
			x['restecg_0.0'] = 0
			x['restecg_1.0'] = 1
			x['restecg_2.0'] = 0
		else:
			x['restecg_0.0'] = 0
			x['restecg_1.0'] = 0
			x['restecg_2.0'] = 1

		#Slope
		slope = np.float(dic['slope'])
		if slope == 1.0:
			x['slope_1.0'] = 1
			x['slope_2.0'] = 0
			x['slope_3.0'] = 0
		elif slope == 2.0:
			x['slope_1.0'] = 0
			x['slope_2.0'] = 1
			x['slope_3.0'] = 0
		else:
			x['slope_1.0'] = 0
			x['slope_2.0'] = 0
			x['slope_3.0'] = 1

		#thal
		thal = np.float(dic['thal'])
		if thal == 3.0:
			x['thal_3.0'] = 1
			x['thal_6.0'] = 0
			x['thal_7.0'] = 0
		elif thal == 6.0:
			x['thal_3.0'] = 0
			x['thal_6.0'] = 1
			x['thal_7.0'] = 0
		else:
			x['thal_3.0'] = 0
			x['thal_6.0'] = 0
			x['thal_7.0'] = 1

		X=pd.DataFrame({'x':x}).transpose()
		return X

	def predict_disease(X):
		model = pkl.load(open('ml_models/heart_diseaseA1.pkl', 'rb'))
		pred = model.predict(X)[0]
		return pred



 