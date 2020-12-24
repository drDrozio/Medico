import tensorflow as tf
from tensorflow import Graph
import tensorflow.keras
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import numpy as np
from tensorflow.keras.models import model_from_json


class covid_ml():
  def preprocess(x):
    img = image.load_img(x, target_size=(224,224))
    img=image.img_to_array(img)
    img=np.expand_dims(img,axis=0)
    return img
  def prediction_disease(img):
  	json_file = open('ml_models/model._corona.json', 'r')
  	loaded_model_json = json_file.read()
  	json_file.close()
  	loaded_model = model_from_json(loaded_model_json)
  	loaded_model.load_weights("ml_models/model_corona.h5")
  	print("Loaded model from disk")
  	p=loaded_model.predict_classes(img)
  	return p[0][0]
    # load weights into new model
	
    #model=load_model('ml_models/modelcovid.h5')