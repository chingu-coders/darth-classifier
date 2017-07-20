#!/usr/bin/python3

# transform images into numpy arrays of shape (no. of images, width, height, 3) 3 represents no.of color channels (RGB) 
# and class labels of shape (no. of images, 1) (labels are 0, 1, 2, 3)

import glob
import pickle
import numpy as np
from scipy import misc

def transform(path, class_label): # create numpy arrays for images and class labels for each darth lord folder
	filelist = glob.glob(path+'/*.jpg')
	images = [misc.imread(img) for img in filelist]
	X = np.array(images)
	y = np.full(len(images), class_label, dtype=int)
	return X, y

maul_X, maul_y = transform('Clean_darth maul', 0)
sidious_X, sidious_y = transform('Clean_darth sidious', 1)
tyranus_X, tyranus_y = transform('Clean_darth tyranus', 2)
vader_X, vader_y = transform('Clean_darth vader', 3)

# concat numpy arrays for images and class labels into their respective arrays
X = np.concatenate((maul_X, sidious_X, tyranus_X, vader_X), axis=0)
y = np.concatenate((maul_y, sidious_y, tyranus_y, vader_y), axis =0)

# pickle numpy arrays
pickle.dump(X, open('images.pkl', 'wb'))
pickle.dump(y, open('labels.pkl', 'wb'))
print('Your pickle files are ready :)')