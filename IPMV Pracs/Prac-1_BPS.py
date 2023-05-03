# Name: Siddhesh Jadhav, Branch: A1, Roll no: 08
import cv2
import numpy as np

a = cv2.imread('doggy.jpg',0)

row,column = a.shape
B_P_S = []
for i in range (a.shape[0]):
    for j in range(a.shape[1]):
        B_P_S.append(np.binary_repr(a[i][j],width=8))

eight_b = (np.array([int(i[0]) for i in B_P_S], dtype=np.uint8)*128).reshape(a.shape[0],a.shape[1])

seventh_b = (np.array([int(i[1]) for i in B_P_S], dtype=np.uint8)*64).reshape(a.shape[0],a.shape[1])

sixth_b = (np.array([int(i[2]) for i in B_P_S], dtype=np.uint8)*32).reshape(a.shape[0],a.shape[1])

fifth_b = (np.array([int(i[3]) for i in B_P_S], dtype=np.uint8)*16).reshape(a.shape[0],a.shape[1])

fourth_b = (np.array([int(i[4]) for i in B_P_S], dtype=np.uint8)*8).reshape(a.shape[0],a.shape[1])

third_b = (np.array([int(i[5]) for i in B_P_S], dtype=np.uint8)*4).reshape(a.shape[0],a.shape[1])

second_b = (np.array([int(i[6]) for i in B_P_S], dtype=np.uint8)*2).reshape(a.shape[0],a.shape[1])

first_b = (np.array([int(i[7]) for i in B_P_S], dtype=np.uint8)*1).reshape(a.shape[0],a.shape[1])

cv2.imshow('Bit_8',cv2.normalize(eight_b,np.zeros(a.shape),0,255,cv2.NORM_MINMAX))

cv2.imshow('Bit_7',cv2.normalize(seventh_b,np.zeros(a.shape),0,255,cv2.NORM_MINMAX))

cv2.imshow('Bit_6',cv2.normalize(sixth_b,np.zeros(a.shape),0,255,cv2.NORM_MINMAX))

cv2.imshow('Bit_5',cv2.normalize(fifth_b,np.zeros(a.shape),0,255,cv2.NORM_MINMAX))

cv2.imshow('Bit_4',cv2.normalize(fourth_b,np.zeros(a.shape),0,255,cv2.NORM_MINMAX))

cv2.imshow('Bit_3',cv2.normalize(third_b,np.zeros(a.shape),0,255,cv2.NORM_MINMAX))

cv2.imshow('Bit_2',cv2.normalize(second_b,np.zeros(a.shape),0,255,cv2.NORM_MINMAX))

cv2.imshow('Bit_1',cv2.normalize(first_b,np.zeros(a.shape),0,255,cv2.NORM_MINMAX))

cv2.waitKey(0)