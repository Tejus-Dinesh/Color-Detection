import cv2
import numpy as np

cap = cv2.VideoCapture(0)
 
# This drives the program into an infinite loop.
while(1):       
    # Captures the live stream frame-by-frame
    _, img = cap.read()
    # img = cv2.imread('/home/dtejus/Desktop/projects/Oasis/signal.jpeg')
    scale_percent = 80 # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    
    # resize image
    img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([10, 100, 20])
    upper_blue = np.array([25, 255, 255])
    lower_red = np.array([0,100,100])
    upper_red = np.array([5,255,255])
    lower_green = np.array([36, 25, 25])
    upper_green = np.array([70, 255,255])
    mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
    res_blue = cv2.bitwise_and(hsv,img, mask= mask_blue)
    mask_green = cv2.inRange(hsv, lower_green, upper_green)
    res_green = cv2.bitwise_and(hsv,img, mask= mask_green)
    mask_red = cv2.inRange(hsv, lower_red, upper_red)
    res_red = cv2.bitwise_and(img,img, mask= mask_red)
    img_concate_Hori=np.concatenate((res_green,res_blue,res_red),axis=1)
    cv2.imshow('Image',img)
    # cv2.imshow('mask',mask)
    # cv2.imshow('res',res_blue)
    # cv2.imshow('res_green', res_green)
    # cv2.imshow('res_red',res_red)
    added_image = cv2.addWeighted(res_red,1.0,res_blue,1.0,0)
    added_image = cv2.addWeighted(added_image,1.0,res_green,0.9,0)
    cv2.imshow('Result',added_image)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
            break
    

    # Destroys all of the HighGUI windows.  
cv2.destroyAllWindows()
cap.release()


