import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"" #install pytesseract module and include the downloaded file path within the inverted commas like "C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"

img = Image.open("") #enter the image filename as "testimage.jpg"
text = pytesseract.image_to_string(img)
print(text)
