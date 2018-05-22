import os
import numpy as np
from keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
from keras.models import Sequential, load_model
import h5py


img_width, img_height = 64, 64
model_path = r'models/model.h5'
model_weights_path = r'models/weights.h5'
model = load_model(model_path)
model.load_weights(model_weights_path)

file = r'a.jpg'

def predict(file):
  x = load_img(file, target_size=(img_width,img_height))
  x = img_to_array(x)
  x = np.expand_dims(x, axis=0)
  array = model.predict(x)
  result = array[0]
  answer = np.argmax(result)
  print(answer)
print(answer)
