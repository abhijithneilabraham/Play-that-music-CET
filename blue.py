#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 23:56:06 2019

@author: abhijithneilabraham
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 00:05:03 2018

@author: abhijithneilabraham
"""

import numpy as np
import cv2

from pygame import mixer
cap = cv2.VideoCapture(0)

i=0


    

while(True):
  # Capture frame-by-frame
   ret, frame = cap.read()
   
   # Our operations on the frame come here
   gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
   blur = cv2.GaussianBlur(gray,(5,5),0)
   ret, thresh_img = cv2.threshold(blur,91,255,cv2.THRESH_BINARY)
   hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV(hue saturation value)
   lower_blue = np.array([110,50,50])
   upper_blue = np.array([130,255,255])

    # Threshold the HSV image to get only blue colors
   mask = cv2.inRange(hsv, lower_blue, upper_blue)

   contours =  cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)[-2]
   
   M = cv2.moments(mask)
   cX = int(M["m10"] / M["m00"])
   cY = int(M["m01"] / M["m00"])
   cv2.circle(frame, (cX, cY), 5, (255, 255, 255), -1)
   cv2.putText(frame, "centroid", (cX - 25, cY - 25),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
   
   for c in contours:
       
       cv2.drawContours(frame, [c], -1, (0,255,0), 3)
       
   p=200
   q=200
   
   if cY>=p and cX>=q:
       
       mixer.init()
       mixer.music.load('bgm_3.mp3')
       mixer.music.play()    
            
      
       
   elif cY>=p and cX<q:
             
       mixer.init()
       mixer.music.load('bgm_4.mp3')
       mixer.music.play()   
           
       
   if cY<p and cX>=q:
       mixer.init()
       mixer.music.load('bgm_2.mp3')
       mixer.music.play() 
      
       
   elif cY<p and cX<q:
       mixer.init()
       mixer.music.load('bgm_2.mp3')
       mixer.music.play()
       
       
     # Display the resulting frame
   cv2.imshow('frame',frame)
   if cv2.waitKey(1) & 0xFF == ord('q'):
       break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
