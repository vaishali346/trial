# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 18:05:25 2019

@author: yashashri_naitam
"""
from PIL import Image
import math
import pytesseract 

def apply_ocr(path):
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
    config = ('-l eng --oem 3 --psm 3')
    x = pytesseract.image_to_string(Image.open(path),config=config)
    with open('C:\Programs\Output\Edited_bajaj_intensity.txt', 'w') as f:
        print(x.encode("utf-8"), file=f)

rgb_img = Image.open(r"C:\Programs\Claimform_bajaj_edited.jpg")
#rgb_img.show(title='Original') 

width = rgb_img.size[0]
height = rgb_img.size[1]

row = 1
col = 1
pix = 0

gray_img=rgb_img.copy()
 
while row < height + 1:
    while col < width + 1:        
        # get the RGB values from the current pixel
        r, g, b = rgb_img.getpixel((col - 1, row - 1))
        grey=math.floor((r+b+g)/3)
        gray_img.putpixel((col - 1, row - 1), (grey,grey,grey))
        col = col + 1
    row = row + 1
    col = 1
 
img_path=r'C:\Programs\Output\grayscaleed_Editedbajaj.jpg'
gray_img.save(img_path)
apply_ocr(img_path)











