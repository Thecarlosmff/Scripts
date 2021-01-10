::https://github.com/UB-Mannheim/tesseract/wiki
::all files in bat loc                              prog                image      out  append  text file
::  for %x in (*) do         D:\Programas\Tesseract-OCR\tesseract.exe    %x      stdout   >>     result.txt
::               -----      FUNCTION     -----
::Convert Image to Text in batch
::               ----- HOW TO USE SCRIPT -----
::1º Create a Folder named "Screenshot" in "C:\"
::2º Download Visual Novel OCR in https://visual-novel-ocr.sourceforge.io
::3º Replace "takeScreenshot.py" in "Visual-Novel-OCR-V2\backendServer" -- do a backup of the original first
::4º Open Visual Novel OCR bat
::5º Click "Generate Text Capture Window"
::6º Take all the needed prints to the text
::7º Download and install Tesseract in https://github.com/UB-Mannheim/tesseract/wiki (for windows) check https://github.com/tesseract-ocr for mac/Linux
::8º Choose the necessary languages
::9º Make sure that Tesseract is in D:\Programas\ if not move it there/change the path below, so the directory to "tesseract.exe" exists
::10º Copy this .bat file to C:\Screenshots
::11º Execute "ImgsToText.bat"
::
::To identify images that ain't clear enough i recommend do a small amount each time.

for %x in (*) do D:\Programas\Tesseract-OCR\tesseract.exe %x stdout >>result.txt
