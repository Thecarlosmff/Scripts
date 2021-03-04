#https://www.python.org/downloads/
#see NumPy Error on Windows
#cmd commands for ^^^:
  #pip install matplotlib
  #pip install numpy
  #pip3 install opencv-python
 
#To execute use:
#                                       "C:\Screenshots\000001"
#C:\Screenshots>py remove_bg_full.py function "000001" 25 255 255 10 10 100 20 "".png"
#       path    ^       file_name     func    ALL ARGUMENTS IN THE SAME ORDER AS IN THE FUNCTION
#for %x in ("C:\Screenshots\images\*") do py remove_bg_simple.py exe %x
#for multiple images:
#
import sys
import os
import numpy as np
import matplotlib.pyplot as plt
import cv2

#try find out if I can choose the number of arguments in a dynamic any otherwise only one function for py
    #limits:
# Max Hue=       179
# Max Saturation=255
# Max Lightness= 255
# Max Hue=       179
# Max Saturation=255
# Max Lightness= 255
def exe(path_img,mH=10,mS=100,mV=20,MH=25,MS=255,MV=255,extension='.png'):
  #array_ignore = np.array([".txt",".py"])
  #array_img = np.array([".png","jpg"])
  subpath ="" #usage:                subpath="subfolder\"
  path_img = path_img.removesuffix(extension)               # Returns the relative/absolute path without the extension
  filename = os.path.basename(path_img)                     # Return the name of the file without extension
  absolute_path = os.path.abspath(path_img)                 # Returns the absolute path
  absolute_path = absolute_path.removesuffix(filename)      # Return directory where the files is

  print("removing background from: "+absolute_path+filename+extension)
  
  mH=int(mH)
  mS=int(mS)
  mV=int(mV)
  MH=int(MH)
  MS=int(MS)
  MV=int(MV)
  
  BGR_image = cv2.imread(path_img+extension) #this transforms the image to BGR, so we will need to change it back
  RGB_image = cv2.cvtColor(BGR_image, cv2.COLOR_BGR2RGB)  
  HSV_image = cv2.cvtColor(RGB_image, cv2.COLOR_RGB2HSV) # convert from RGB to HSV

  lower_array = np.array([mH, mS, mV])
  upper_array = np.array([MH, MS, MV])

  mask = cv2.inRange(HSV_image, lower_array, upper_array)
 
  cv2.imwrite(absolute_path+subpath+"mod_"+filename+extension,mask)
  cv2.waitKey();cv2.destroyAllWindows()

#for everything:
if __name__ == '__main__':
    globals()[sys.argv[1]](sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6],sys.argv[7],sys.argv[8],sys.argv[9])