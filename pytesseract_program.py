
from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
config = ('-l eng --oem 3 --psm 3')


x=pytesseract.image_to_string(Image.open(r'C:\Programs\code\14.jpg'),config=config)
print(x)
with open(r'C:\Programs\Output\outofPyTesseract.txt', 'w') as f:
    print(x.encode('utf-8'), file=f)

