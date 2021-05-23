import cv2
import numpy as np
import matplotlib.pyplot as plt
# tên biến theo đúng đề bài
I = cv2.imread("7.jpg")

#23a
cv2.imshow('anh input',I)
#1
h = I.shape[0];
w = I.shape[1]
Ig=cv2.cvtColor(I,cv2.COLOR_BGR2GRAY)
Ig = np.zeros((h, w), dtype='uint8')
for i in range (h):
	for j in range (w):
		#gray = 0.39*r + 0.50*g + 0.11*b
		d = 39*int(I[i][j][2]) + 50*int(I[i][j][1]) + 11*(I[i][j][0])
		d = d//100
		Ig[i][j]=d
cv2.imshow('anh gray',Ig)
#2
nguong_otsu, Ib = cv2.threshold(Ig,0,255, cv2.THRESH_OTSU) 
print(nguong_otsu)
cv2.imshow('anh nhi phan bang Otsu',Ib)
#4
h=Ig.shape[0]
w=Ig.shape[1]
Im=cv2.blur(Ig,(3,3))
cv2.imshow('anh tron',Im)
cv2.waitKey()