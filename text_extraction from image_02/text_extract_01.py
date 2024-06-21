from PIL import Image
from pytesseract import pytesseract
import os

# Defining paths to tesseract.exe
# and the image we would be using
path_to_tesseract = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
image_path = r"csv\sampletext.png"

# Opening the image & storing it in an image object
img = Image.open(image_path)

# Providing the tesseract executable
# location to pytesseract library
pytesseract.tesseract_cmd = path_to_tesseract

# Passing the image object to image_to_string() function
# This function will extract the text from the image
text = pytesseract.image_to_string(img)

# Displaying the extracted text
print(text[:-1])

# Defining the path for the output text file
output_text_path = os.path.splitext(image_path)[0] + ".txt"

# Writing the extracted text to the new text file
with open(output_text_path, "w", encoding="utf-8") as text_file:
    text_file.write(text)
