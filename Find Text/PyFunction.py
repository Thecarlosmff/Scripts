import os
import sys
import numpy as np
import matplotlib.pyplot as plt
import cv2

def get_info(path_img,list):
        info = [0,"","","",""]
        info[1], info[2] = os.path.splitext(path_img)
        if(info[2] ==""):
                info[0] = 1 #print("Enter a file extension (e.g. name.png)")
                return info
        if(info[2] not in list):
                info[0] = 2 #print("Not an image")
                return info

        info[3] = info[1]
        info[1] = os.path.basename(info[3])                     # Return the name of the file without extension
        info[4] = os.path.abspath(info[3])                 # Returns the absolute path
        info[4] = info[4].removesuffix(info[1])      # Return directory where the files is

        if(os.path.exists(info[4]+info[1]+info[2]) == False):
                info[0] = 3     #print (info[4]+info[1]+info[2] + " not found!")
        # 0 - error     1-No extension  2- Not a image  3- Not found
        # 1 - filename        # 2 - file_extension        # 3 - path_img        # 4 - absolute_path
        #print(info)
        return info

class ImageToText:
    @staticmethod
    def remove_bg(path_img,mH=0,mS=0,mV=200,MH=179,MS=55,MV=255, subpath = ""):
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
        if(path_img == "-h"):
                print("How it works?")  
                print("   It uses the HSV color system to find a specific color and isolate it")
                print("   is it perfect? Of course not similar colors can affect the process")
                print("   you can look in the internet to learn how to choose the right values")
                print("")
                print("Some commands:")
                print("   -usage        Show the possible parametres")
                print("   -colors       Shows some default colors (those numbers can be improved, they are just a reference)")
                return  
        if(path_img == "-colors"):
                print("A few colors     mH |mS |mV |MH |MS |MV ")
                print("White            0  | 0 |200|179|55 |255")
                print("Red                 |   |   |   |   |   ")
                print("Blue                |   |   |   |   |   ")
                print("Green               |   |   |   |   |   ")
                print("Black               |   |   |   |   |   ")
                print("Yellow              |   |   |   |   |   ")
                print("Orange   |   |   |   |   |   ")
                print("Pink   |   |   |   |   |   ")
                print("Light Red   |   |   |   |   |   ")
                print("Dark Red   |   |   |   |   |   ")
                print("Light Blue   |   |   |   |   |   ")
                print("Dark Blue   |   |   |   |   |   ")
                print("Light Green   |   |   |   |   |   ")
                print("Dark Green   |   |   |   |   |   ")
                return
        array_img = np.array([".png",".jpg"])
        info = get_info(path_img,array_img)
        if(info[0]==1):
                print("Enter a file extension (e.g. name.png)")
                return
        if(info[0]==2):
                print("Not an image")
                return
        if(info[0]==3):
                print (info[4]+info[1]+info[2] + " not found!")
                return
        print("removing background from: "+info[4]+info[1]+info[2])
  
        mH=int(mH)
        mS=int(mS)
        mV=int(mV)
        MH=int(MH)
        MS=int(MS)
        MV=int(MV)

        BGR_image = cv2.imread(info[3]+info[2]) #this transforms the image to BGR, so we will need to change it back
        HSV_image = cv2.cvtColor(BGR_image, cv2.COLOR_BGR2HSV) # convert from RGB to HSV
        #Treat the values in case that the min > max
        if(MH>=mH and MS>=mS and MV>=mV): #everything is correct
                lower_array = np.array([mH, mS, mV],dtype=np.uint8)
                upper_array = np.array([MH, MS, MV],dtype=np.uint8)
                mask = cv2.inRange(HSV_image, lower_array, upper_array)
        elif(MH<mH and MS>=mS and MV>=mV): #Only Hue Wrong
                lower_array = np.array([0, mS, mV],dtype=np.uint8)
                upper_array = np.array([MH, MS, MV],dtype=np.uint8)
                mask = cv2.inRange(HSV_image, lower_array, upper_array)

                lower_array = np.array([mH, mS, mV],dtype=np.uint8)
                upper_array = np.array([179, MS, MV],dtype=np.uint8)
                mask += cv2.inRange(HSV_image, lower_array, upper_array)      
        elif(MH>mH and MS<mS and MV>=mV): #Only Saturation Wrong     0 240 0 0 10 0
                lower_array = np.array([mH, 0, mV],dtype=np.uint8)
                upper_array = np.array([MH, MS, MV],dtype=np.uint8)
                mask = cv2.inRange(HSV_image, lower_array, upper_array)

                lower_array = np.array([mH, mS, mV],dtype=np.uint8)
                upper_array = np.array([MH, 255, MV],dtype=np.uint8)
                mask += cv2.inRange(HSV_image, lower_array, upper_array)
        elif(MH>=mH and MS>=mS and MV<mV): #Only Value Wrong           0 0 240 0 0 10
                lower_array = np.array([mH, mS, 0],dtype=np.uint8)
                upper_array = np.array([MH, MS, MV],dtype=np.uint8)
                mask = cv2.inRange(HSV_image, lower_array, upper_array)

                lower_array = np.array([mH, mS, mV],dtype=np.uint8)
                upper_array = np.array([MH, MS, 255],dtype=np.uint8)
                mask += cv2.inRange(HSV_image, lower_array, upper_array)
        elif(MH<mH and MS<mS and MV>=mV): #Hue and Saturation                   170 250 0 5 10 0
                lower_array = np.array([0, 0, mV],dtype=np.uint8)                              
                upper_array = np.array([MH, MS, MV],dtype=np.uint8)                      
                mask = cv2.inRange(HSV_image, lower_array, upper_array)                 #0-5 & 0-10
                                                                          
                lower_array = np.array([0, mS, mV],dtype=np.uint8)
                upper_array = np.array([MH, 255, MV],dtype=np.uint8)
                mask += cv2.inRange(HSV_image, lower_array, upper_array)                 #0-5 & 250-255  

                lower_array = np.array([mH, 0, mV],dtype=np.uint8)
                upper_array = np.array([179, MS, MV],dtype=np.uint8)
                mask += cv2.inRange(HSV_image, lower_array, upper_array)                 #170-179 & 0-10

                lower_array = np.array([mH, mS, mV0],dtype=np.uint8)
                upper_array = np.array([179, 255, MV],dtype=np.uint8)
                mask += cv2.inRange(HSV_image, lower_array, upper_array)                #   170-179 & 250-255
        elif(MH<mH and MS>=mS and MV<mV): #Hue and Value
                lower_array = np.array([0, mS, 0],dtype=np.uint8)
                upper_array = np.array([MH, MS, MV],dtype=np.uint8)
                mask = cv2.inRange(HSV_image, lower_array, upper_array)

                lower_array = np.array([0, mS, mV],dtype=np.uint8)
                upper_array = np.array([MH, MS, 255],dtype=np.uint8)
                mask += cv2.inRange(HSV_image, lower_array, upper_array)

                lower_array = np.array([mH, mS, 0],dtype=np.uint8)
                upper_array = np.array([179, MS, MV],dtype=np.uint8)
                mask += cv2.inRange(HSV_image, lower_array, upper_array)
                
                lower_array = np.array([mH, mS, mV],dtype=np.uint8)
                upper_array = np.array([179, MS, 255],dtype=np.uint8)
                mask += cv2.inRange(HSV_image, lower_array, upper_array) 
        elif(MH>=mH and MS<mS and MV<mV): #Value and Saturation
                lower_array = np.array([mH, 0, 0],dtype=np.uint8)
                upper_array = np.array([MH, MS, MV],dtype=np.uint8)
                mask = cv2.inRange(HSV_image, lower_array, upper_array)

                lower_array = np.array([mH, 0, mV],dtype=np.uint8)
                upper_array = np.array([MH, MS, 255],dtype=np.uint8)
                mask += cv2.inRange(HSV_image, lower_array, upper_array)

                lower_array = np.array([mH, mS, 0],dtype=np.uint8)
                upper_array = np.array([MH, 255, MV],dtype=np.uint8)
                mask += cv2.inRange(HSV_image, lower_array, upper_array)
                
                lower_array = np.array([mH, mS, mV],dtype=np.uint8)
                upper_array = np.array([MH, 255, 255],dtype=np.uint8)
                mask += cv2.inRange(HSV_image, lower_array, upper_array) 
        elif(MH<mH and MS<mS and MV<mV): #everything is wrong
                lower_array = np.array([0, 0, 0],dtype=np.uint8)
                upper_array = np.array([MH, MS, MV],dtype=np.uint8)
                mask = cv2.inRange(HSV_image, lower_array, upper_array) 

                lower_array = np.array([0, 0, mV],dtype=np.uint8)
                upper_array = np.array([MH, MS, 255],dtype=np.uint8)
                mask += cv2.inRange(HSV_image, lower_array, upper_array)

                lower_array = np.array([0, mS, 0],dtype=np.uint8)
                upper_array = np.array([MH, 255, MV],dtype=np.uint8)
                mask += cv2.inRange(HSV_image, lower_array, upper_array)

                lower_array = np.array([mH, 0, 0],dtype=np.uint8)
                upper_array = np.array([MH, 255, MV],dtype=np.uint8)
                mask += cv2.inRange(HSV_image, lower_array, upper_array)

                lower_array = np.array([mH, mS, 0],dtype=np.uint8)
                upper_array = np.array([179, 255, MV],dtype=np.uint8)
                mask += cv2.inRange(HSV_image, lower_array, upper_array)
                
                lower_array = np.array([mH, 0, mV],dtype=np.uint8)
                upper_array = np.array([179, MS, 255],dtype=np.uint8)
                mask += cv2.inRange(HSV_image, lower_array, upper_array)

                lower_array = np.array([0, mS, mV],dtype=np.uint8)
                upper_array = np.array([MH, 255, 255],dtype=np.uint8)
                mask += cv2.inRange(HSV_image, lower_array, upper_array)

                lower_array = np.array([mH, mS, mV],dtype=np.uint8)
                upper_array = np.array([179, 255, 255],dtype=np.uint8)
                mask += cv2.inRange(HSV_image, lower_array, upper_array) 

        #lower_array = np.array([mH, mS, mV],dtype=np.uint8)
        #upper_array = np.array([MH, MS, MV],dtype=np.uint8)
        #mask = cv2.inRange(HSV_image, lower_array, upper_array)

        cv2.imwrite(info[4]+subpath+"mod_"+info[1]+info[2],mask)

        cv2.waitKey();cv2.destroyAllWindows()

    @staticmethod
    def remove_bg_rgb(path_img):
        subpath = ""
        array_img = np.array([".png","jpg"])
        info = get_info(path_img,array_img)
        if(info[0]==1):
                print("Enter a file extension (e.g. name.png)")
                return
        if(info[0]==2):
                print("Not an image")
                return
        if(info[0]==3):
                print (info[4]+info[1]+info[2] + " not found!")
                return
        print("removing background from: "+info[4]+info[1]+info[2])

        lower_array = np.array([210, 210, 210],dtype=np.uint8) #Blue, Green, Red
        upper_array = np.array([255, 255, 255],dtype=np.uint8) #Blue, Green, Red
        BGR_image = cv2.imread(info[3]+info[2])
        mask = cv2.inRange(BGR_image, lower_array, upper_array)
        #output = cv2.bitwise_and(BGR_image, BGR_image, mask = mask)
        cv2.imwrite(info[4]+subpath+"mod_"+info[1]+info[2],mask)
        #cv2.imwrite(absolute_path+subpath+"mod_"+filename+file_extension,output)

        cv2.waitKey();cv2.destroyAllWindows()

    @staticmethod
    def to_gray(path_img):
        subpath = ""
        array_img = np.array([".png","jpg"])
        info = get_info(path_img,array_img)
        if(info[0]==1):
                print("Enter a file extension (e.g. name.png)")
                return
        if(info[0]==2):
                print("Not an image")
                return
        if(info[0]==3):
                print (info[4]+info[1]+info[2] + " not found!")
                return
        print("Turning "+info[4]+info[1]+info[2]+" to gray.")

        BGR_image = cv2.imread(info[3]+info[2])
        RGB_image = cv2.cvtColor(BGR_image, cv2.COLOR_BGR2RGB)
        gray = np.dot(RGB_image[...,:3], [0.2989, 0.5870, 0.1140])

        cv2.imwrite(info[4]+subpath+"gray_"+info[1]+info[2],gray)

        cv2.waitKey();cv2.destroyAllWindows()
    
