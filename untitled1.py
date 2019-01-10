import numpy as np
import cv2
import random
from pygame import mixer # Load the required library

cap = cv2.VideoCapture(0) #This enables the camera.The value 1 is for external camera,0 for internal camera
p=100
i=0







while True:

    

    
    ret, frame = cap.read()  #returns ret=either true or false. the frame variable has the frames 
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 
    '''
    why did we convert to hsv ? because while using BGR,we have to use 3 values for color combinations(eg.(255,90,30))
    But in case of hsv,for getting the required color,we have to change only one parameter,that is ,hue ,and the two other parameters can be changed just to change the saturation and values.
    '''
    blur = cv2.GaussianBlur(hsv,(5,5),5)
    '''
    The blurring is set to high here. we did blurring because,blurring eliminates the image noise and  reduce detail.
    '''
    
    lower_orange = np.array([0,150,150])#see,the hue from 0,30 is used here for orange,but remeber to set the other values too according to your need.If the other two values are zero,then you will get black because of zero intensity
    upper_orange = np.array([30,255,255])
    mask = cv2.inRange(blur, lower_orange, upper_orange)
    '''
    the color from lower orange to upper orange is noted here.
    '''
    ret, thresh_img = cv2.threshold(mask,91,255,cv2.THRESH_BINARY)
    '''
    
    
    
    Here, the matter is straight forward. 
    If pixel value is greater than a threshold value, it is assigned one value (may be white), else it is assigned another value (may be black). 
    The function used is cv.threshold. First argument is the source image, which should be a grayscale image. 
    Second argument is the threshold value which is used to classify the pixel values. 
    Third argument is the maxVal which represents the value to be given if pixel value is more than (sometimes less than) the threshold value. 
    OpenCV provides different styles of thresholding and it is decided by the fourth parameter of the function. 
    
    
    
    
    '''
    
    contours =  cv2.findContours(thresh_img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)[-2]#ah,the cool fun part!draw contours over the required orange area!
    '''
    I gave the parameter thresh_img here as input. If I gave frame as input I would get contours for every shape in the camera.
    But by masking and thresholding, I have concentrated my interests into just the orange area .
    '''
    M = cv2.moments(mask)
    if M["m00"]!=0 :
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
#These moments and cX and cY ,i used to draw centroids.I will be using the centroid of the orange area.
    cv2.circle(frame, (cX, cY), 5, (255, 255, 255), -1)
    cv2.putText(frame, "centroid", (cX - 25, cY - 25),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    for c in contours:
        cv2.drawContours(frame, [c], -1, (0,255,0), 3)#in previous function of contours i just only found contours. Now here I am drawing
   
    p=200
    i=0
    if cY>=p:
        

        mixer.init()
        mixer.music.load('bgm_2.mp3')
        mixer.music.play()
            
        p=cY
    else:
        mixer.init()
        mixer.music.load('bgm_3.mp3')
        mixer.music.play()
        p=cY
       
    '''
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            keydown(event)
        elif event.type == KEYUP:
            keyup(event)
        elif event.type == QUIT:
            pygame.quit()
            sys.exit()
            '''
   
    
cap.release()#release the camera beast
cv2.destroyAllWindows()
