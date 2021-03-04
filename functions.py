#NOT TESTED
#https://www.python.org/downloads/
#see NumPy Error on Windows
#cmd commands for ^^^:
  #pip install matplotlib
  #pip install numpy
  #pip3 install opencv-python
 
#To execute use:
#C:\Screenshots>py functions.py copy_all     arg1     agr2
#       path    ^   file_name   function    
import sys
import os
import numpy as np
import matplotlib.pyplot as plt
import cv2

def test():
  print("This is a test.")

def test_a(input1="None"):
  print("input1= "+ input1)

def test_b(input1,input2="Hello"):
  print("input1= "+ input1)
  print("input2= "+ input2)

#if __name__ == '__main__':
#  globals()[sys.argv[1]]()


#for the image name only:
if __name__ == '__main__':
    globals()[sys.argv[1]](sys.argv[2])

#for everything:
#if __name__ == '__main__':
#    globals()[sys.argv[1]](sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6],sys.argv[7],sys.argv[8],sys.argv[9])