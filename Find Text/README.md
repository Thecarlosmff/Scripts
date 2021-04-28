#  Text recognition

## Instructions
### 1. Capture and treatment of images
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
    * If the path uses SPACES use **""**, like this **"C:\My Images\image9.png"**
    * This will use the default setting and apply them to the image in question.
9. Another example:
    * **py PyRun.py PyFunction.ImageToText.remove_bg image23.png 0 5 130 20 70 255 clean/**
    * This command will look for colors that the Hue is above 0 and below 20, the saturation is between 5 and 70. While the color is between 130 and 255, for last will save the new image on a subdirectory called clean.
    * type **py PyRun.py PyFunction.ImageToText.remove_bg -usage** to check what is what.
    * [HSV - Image](https://upload.wikimedia.org/wikipedia/commons/thumb/3/33/HSV_color_solid_cylinder_saturation_gray.png/1280px-HSV_color_solid_cylinder_saturation_gray.png), use the -usage to see limits
10. For batch background remover:
    * **for %x in ("C:\Screenshots\\*") do py PyRun.py PyFunction.ImageToText.remove_bg "%x"** assuming that the images are at "C:\Screenshots\\"

### 2. Image to Text
1. Download [Tesseract-OCR](https://github.com/UB-Mannheim/tesseract/wiki) This program allows OCR, assuming that the image is clear (it works anyways but more prone to mistakes).
2. Install Tesseract-OCR, select the necessary languages and take note of the installation path particularly the location of **tesseract.exe**. In my case, the path is **D:\Programas\Tesseract-OCR\tesseract.exe**
3. Open the command line.
4. In the command line go to the images path (in my case **C:\Screenshots**) using **cd ABSOLUTE_PATH** (f.e. *cd C:\Screenshots*)
5. To "convert" all images to text in the command line use **for %x in (*) do TESSERACT.EXE_PATH %x stdout >>OUTPUT_FILE -l LANG**
    * So **for %x in (*) do D:\Programas\Tesseract-OCR\tesseract.exe %x stdout >>result.txt** (english, with my settings)
    * **for %x in (*) do D:\Programas\Tesseract-OCR\tesseract.exe %x stdout >>result.txt -l jpn** (japonese, my settings)
    * Note: If paths use SPACES use "", like "C:\My Images" instead of C:\My Images
##### To excel
6. The text should be on your output file the text of each image is separated by a character that in docx files (Word) is the equivalent to a *break page*
7. Open the output file (usually a txt file), select all the text and create a new docx file (new file in the word).
8. Copy all the text to the word.
9. Create/open the excel file and download the **Export Word to Excel (OCR).bas** file.
10. If needed enable the devolper tab in the excel. [Here](https://support.microsoft.com/en-us/topic/show-the-developer-tab-e1192344-5e56-4d45-931b-e5fd9bea2d45)
11. Click **Save as** and as the type of file select **Worksheet with permission for Excel Macros** (I tried to translate it myself not sure if those are the exact words)
12. In the devolper click in **Visual Basic** -> **Tools** -> **References**
13. Check the fowlling boxes:
     * **Visual Basic for Applications** is likelly already checked
     * **Microsoft Excel 16.0 Object Library** is likelly already checked (version may differ)
     * **OLE Automation** is likelly already checked
     * **Microsoft Office 16.0 Object Library** is likelly already checked
     * **Microsoft Word 16.0 Object Library** Important
14. In the **Visual Basic** go to **File** -> **Import file** and import the downloaded "bas" file
15. In the modules section select the subrotine and change the line:
     * **Set objDoc = objWord.documents.Open("C:\test.docx")** to match your docx file
     * Press **Ctrl + S** to Save
16. Press **F5** to run the Sub or click on the play
     * The script will separate each image text for a row.
     * The text will be on the active sheet.
     * If you need to run more than one word file do it in a new sheet otherwise overwrites the previous text.
     * If you want to add the text in the same page but starting on the line 100 in the script change the line **j = 1** to **J = 100**
     * To change the collumn just change the variable **Col = 1** to **Col = 3** to put the text in the "C" collumn, A = 1, B = 2, C = 3...
     * To format how the text works the main thing to have in consideration is that the script checks letter by letter
     * chr(12) is a break page, chr(13) is a new line


#### Useful links
* [Tacking White Color](https://stackoverflow.com/questions/22588146/tracking-white-color-using-python-opencv)
* [Working with Tesseract ORC](https://stackoverflow.com/questions/26251599/can-i-test-tesseract-ocr-in-windows-command-line)
* [HSV - Image](https://upload.wikimedia.org/wikipedia/commons/thumb/3/33/HSV_color_solid_cylinder_saturation_gray.png/1280px-HSV_color_solid_cylinder_saturation_gray.png)

#### Tips
1. A very images useful to test ranges
    * [Depth Color Wheel Photography Theory - Magenta - Vector Hand-drawn Ring Transparent PNG](https://pnghut.com/png/N4yMSmTZ2H/depth-color-wheel-photography-theory-magenta-vector-hand-drawn-ring-transparent-png)
    * [Color Wheel Colorfulness Theory HSL And HSV - Scheme - Hue Transparent PNG](https://pnghut.com/png/Dqvm1ui1NS/color-wheel-colorfulness-theory-hsl-and-hsv-scheme-hue-transparent-png)
    * [Color Wheel Complementary Colors Scheme Analogous - Of Lead Transparent PNG](https://pnghut.com/png/qCC1gGhWJn/color-wheel-complementary-colors-scheme-analogous-of-lead-transparent-png)
    * [Color Wheel Complementary Colors - Hue Ring Chart Transparent PNG](https://pnghut.com/png/sutZgai9HB/color-wheel-complementary-colors-hue-ring-chart-transparent-png) BEST
    * [Color Wheel Complementary Colors Scheme Theory - Analogous - Paint Transparent PNG](https://pnghut.com/png/0BPfpmx6ZE/color-wheel-complementary-colors-scheme-theory-analogous-paint-transparent-png)
    * [Color Wheel Creativity Interior Design Services - Complementary Colors - Colour Transparent PNG](https://pnghut.com/png/wQTaMkMf0D/color-wheel-creativity-interior-design-services-complementary-colors-colour-transparent-png)
2. Examples:
    * [Find the right numbers](https://github.com/Thecarlosmff/Scripts/tree/main/Find%20Text/Images/Colors)
    * [Extracted Text]()
