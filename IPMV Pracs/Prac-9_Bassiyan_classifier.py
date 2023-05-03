# Name: Siddhesh Jadhav, Batch: A1, Roll-no: 08

import ssl
ssl.create_default_https_context = ssl._create_unverified_context
from tensorflow import keras
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import numpy as np
from sklearn.naive_bayes import GaussianNB
import cv2
(x_train, y_train), (x_test, y_test) = keras.datasets.cifar10.load_data()
x_train.shape,x_test.shape

# Normalisation 
x_train = x_train/255.0
x_test = x_test/255.0
nsamples, nx,ny,nrgb = x_train.shape
x_train2 = x_train.reshape((nsamples, nx*ny*nrgb))
nsamples, nx,ny,nrgb = x_test.shape
x_test2 = x_test.reshape((nsamples, nx*ny*nrgb))

nb = GaussianNB()
nb.fit(x_train2, y_train)

y_pred_nb = nb.predict(x_test2)
y_pred_nb

accuracy_score(y_pred_nb, y_test)
print(classification_report(y_pred_nb, y_test))