###  Text recognition

## Instructions
1. Download [Greenshot](https://getgreenshot.org/downloads/), it allows take fast partial screenshots.
2. Download [Python 3.9](https://www.python.org/downloads/) may not work in older versions. (Take mental note of the local of instalation)
3. Unless you have/already use Python you will need to do the following:
   * Go to Python installation directory usually (C:\Users\USERNAME\AppData\Local\Programs\Python\PythonXX\Scripts) or (C:\Program Files (x86\PythonXX\Scripts).
   * Select copy the address in the top (absoulte path).
   * Open the command line with administator right (Win > write "cmd" > right click > run as admin).
   * In the command line write **cd C:\Users\USERNAME\AppData\Local\Programs\Python\PythonXX\Scripts**              (for example)
   * Write **pip install matplotlib** press enter and wait.
   * Write **pip install numpy** press enter and wait.
   * Write **pip3 install opencv-python** press enter and wait.
4. Download **PyRun.py** and **PyFunction.py** present in this directory
5. Copy the two downloaded files to your images directory. Copy the absolute path in the top. (for example *C:\Screenshots*)
6. Open another command line and type **cd C:\Screenshots** (using the example in 5).
7. Now all should be ready to start, some examples next.
8. To excute the function type *py PyRun.py PyFunction.ImageToText.remove_bg NAME.EXT*
    * **py PyRun.py PyFunction.ImageToText.remove_bg image23.png**
                        or using the absolute path
    * **py PyRun.py PyFunction.ImageToText.remove_bg C:\Screenshots\image23.png**
    * If the path uses SPACES put use **""**, like this **"C:\My Images\image9.png"**
    * This will use the default setting and apply them to the image in question.
9. Another example:
    * **py PyRun.py PyFunction.ImageToText.remove_bg image23.png 0 5 130 20 70 255 clean/**
    * This command will look for colors that the Hue is above 0 and below 20, the saturation is between 5 and 70. While the color is between 130 and 255, for last will save the new image on a subdirectory called clean.
    * type **py PyRun.py PyFunction.ImageToText.remove_bg -usage** to check what is what.
    * [HSV - Image](https://upload.wikimedia.org/wikipedia/commons/thumb/3/33/HSV_color_solid_cylinder_saturation_gray.png/1280px-HSV_color_solid_cylinder_saturation_gray.png), use the -usage to see limits
10. For batch background remover:
    * **for %x in ("C:\Screenshots\*") do py PyRun.py PyFunction.ImageToText.remove_bg "%x"** assuming that the images are at "C:\Screenshots\"


#### Useful links
* [Tacking White Color](https://stackoverflow.com/questions/22588146/tracking-white-color-using-python-opencv)
* [Working with Tesseract ORC](https://stackoverflow.com/questions/26251599/can-i-test-tesseract-ocr-in-windows-command-line)
* [HSV - Image](https://upload.wikimedia.org/wikipedia/commons/thumb/3/33/HSV_color_solid_cylinder_saturation_gray.png/1280px-HSV_color_solid_cylinder_saturation_gray.png)
