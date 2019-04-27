# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 22:21:08 2019

@author: NEBU
"""

import os
import numpy as np
from keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
from keras.models import Sequential, load_model
from keras.preprocessing import image
import time
import cv2

start = time.time()

#Define Path
model_path = './models/model.h5'
model_weights_path = './models/weights.h5'
test_path = './data/validation'

#Load the pre-trained models
model = load_model(model_path)
model.load_weights(model_weights_path)

#Define image parameters
img_width, img_height = 150,150

from tkinter.filedialog import askopenfilename
img_path = askopenfilename()

test_image = image.load_img(img_path, target_size = (150,150))
test_image1 = image.img_to_array(test_image)
test_image2 = np.expand_dims(test_image1, axis = 0)
array = model.predict(test_image2)
result = array[0]
  #print(result)
answer = np.argmax(result)
if answer == 1:
    print("Predicted: Fear")
elif answer == 0:
    print("Predicted: Anger")
elif answer == 2:
    print("Predicted: Happy")
elif answer == 3:
    print("Predicted: Neutral")
"""
#Prediction Function
def predict(file):
  x = load_img(file, target_size=(img_width,img_height))
  x = img_to_array(x)
  x = np.expand_dims(x, axis=0)
  array = model.predict(x)
  result = array[0]
  #print(result)
  answer = np.argmax(result)
  if answer == 1:
    print("Predicted: 1")
  elif answer == 0:
    print("Predicted: 2")
  elif answer == 2:
    print("Predicted: 3")
  elif answer == 3:
    print("Predicted: xxxxxxxxx")

  return answer

#Walk the directory for every image
for i, ret in enumerate(os.walk(test_path)):
  for i, filename in enumerate(ret[2]):
    if filename.startswith("."):
      continue
    
    print(ret[0] + '/' + filename)
    result = predict(ret[0] + '/' + filename)
    print(" ")
"""
#Calculate execution time
end = time.time()
dur = end-start
"""
if dur<60:
    print("Execution Time:",dur,"seconds")
elif dur>60 and dur<3600:
    dur=dur/60
    print("Execution Time:",dur,"minutes")
else:
    dur=dur/(60*60)
print("Execution Time:",dur,"hours")
"""