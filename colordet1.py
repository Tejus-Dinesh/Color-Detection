import cv2
import numpy as np
img = cv2.imread('/home/dtejus/Desktop/projects/Oasis/Abstract_Rainbow.jpg')
scale_percent = 30 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
  
# resize image
img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower_range = np.array([0,100,100])
upper_range = np.array([5,255,255])
mask = cv2.inRange(hsv, lower_range, upper_range)
cv2.imshow('image_window_name', img)
cv2.imshow('mask_window_name', mask)
cv2.waitKey(0)
cv2.destroyAllWindows()