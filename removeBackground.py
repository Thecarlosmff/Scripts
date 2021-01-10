#NOT TESTED

import numpy as np
import matplotlib.pyplot as plt
import cv2

def remove_background(path_img,maxSat,maxBri,maxColor,minSat=0,minBri=0,minColor=0,extension='.png'):
  print("Hello from a function")
  
  
  BGR_image = cv2.imread(path_img+extension) #this transforms the image to BGR, so we will need to change it back
  RGB_image = cv2.cvtColor(ball, cv2.COLOR_BGR2RGB)
  
  
  # convert from RGB to HSV
  HSV_image = cv2.cvtColor(tongue, cv2.COLOR_RGB2HSV)
#  h = HSV_image[:,:,0]
#  s = HSV_image[:,:,1]
#  v = HSV_image[:,:,2]
  
  mask = cv2.inRange(HSV_image,(10, 100, 20), (25, 255, 255) ) #change for the actual values
  
  cv2.imwrite(path_img+'mod'+extension,mask)
  #cv2.imshow("orange", mask);
  cv2.waitKey();cv2.destroyAllWindows()
  
remove_background("image",179,255,255,0,0,0)
