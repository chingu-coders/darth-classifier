# -*- coding: utf-8 -*-
from keras.models import load_model

classifier = load_model("darth.h5")

import cv2
import numpy as np
img = cv2.imread('vader.jpg')
img = cv2.resize(img,(64, 64))
img = np.reshape(img,(1, 64, 64, 3))

mapper = ["Maul","Sidious","Tyranous","Vader"]

print(mapper[classifier.predict_classes(img)[0]])