import os
import sys
import numpy as np
import matplotlib.pyplot as plt
import cv2
    
class ImageToText:
    @staticmethod
    def remove_bg(path_img,mH=0,mS=0,mV=245,MH=255,MS=10,MV=255, subpath = ""):
        #py PyRun.py PyFunction.ImageToText.remove_bg 000012.png
        if(path_img == "-usage"):
                print ("USAGE:")
                print ("        remove_bg path_img minHue minSat MinVal MaxHue MaxSat MaxVal subpath")
                print ("        py PyRun.py PyFunction.ImageToText.remove_bg C:\image.png 0 23 45 30 40 255 new/")
                print ("")
                print ("path_img:        image path Mandatory   relative or absolute")
                print ("Min Hue          0-179      Opcional")
                print ("Min Saturation   0-255      Opcional")
                print ("Min Value        0-255      Opcional")
                print ("Max Hue          0-179      Opcional")
                print ("Max Saturation   0-255      Opcional")
                print ("Max Value        0-255      Opcional")
                print ("Subpath          name\      Opcional    must end with \ ")
                return
        if(path_img == "-help"):
                print("How it works?")  
                print("   It uses the HSV color system to find a specific color and isolate it")
                print("   is it perfect? Of course not similar colors can affect the process")
                print("   you can look in the internet to learn how to choose the right values")
                return  
        #array_ignore = np.array([".txt",".py"])
        array_img = np.array([".png","jpg"])

        filename, file_extension = os.path.splitext(path_img)
        #print(filename)
        #print(file_extension)
        if(file_extension not in array_img):
                if(file_extension ==""):
                        print("Enter a file extension (e.g. name.png)")
                        return
                print("Not an image")
                return
        path_img = filename
        #print(path_img)
        filename = os.path.basename(path_img)                     # Return the name of the file without extension
        #print(filename)
        absolute_path = os.path.abspath(path_img)                 # Returns the absolute path
        #print(absolute_path)
        absolute_path = absolute_path.removesuffix(filename)      # Return directory where the files is
        #print(absolute_path)

        if(os.path.exists(absolute_path+filename+file_extension) == False):
                print (absolute_path+filename+file_extension + " not found!")
                return
        print("removing background from: "+absolute_path+filename+file_extension)
  
        mH=int(mH)
        mS=int(mS)
        mV=int(mV)
        MH=int(MH)
        MS=int(MS)
        MV=int(MV)
  
        BGR_image = cv2.imread(path_img+file_extension) #this transforms the image to BGR, so we will need to change it back
        RGB_image = cv2.cvtColor(BGR_image, cv2.COLOR_BGR2RGB) 
        HSV_image = cv2.cvtColor(RGB_image, cv2.COLOR_RGB2HSV) # convert from RGB to HSV

        lower_array = np.array([mH, mS, mV],dtype=np.uint8)
        upper_array = np.array([MH, MS, MV],dtype=np.uint8)

        mask = cv2.inRange(HSV_image, lower_array, upper_array)
 
        cv2.imwrite(absolute_path+subpath+"mod_"+filename+file_extension,mask)
        cv2.waitKey();cv2.destroyAllWindows()