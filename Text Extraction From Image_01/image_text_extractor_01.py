# Importing all required libraries
import os
import cv2
import numpy as np
from PIL import Image
import pytesseract

# Set the Tesseract executable path if not in PATH
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

# Function to process the image and extract text
def extract_text_from_image(image_path, output_dir):
    # Reading the image using OpenCV
    img = cv2.imread(image_path)
    if img is None:
        print(f"Failed to read {image_path}")
        return

    # Convert image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply threshold to get binary image
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)

    # Save the processed image for verification
    processed_image_path = os.path.join(output_dir, "processed_image.png")
    cv2.imwrite(processed_image_path, thresh)
    print(f"Processed image saved to: {processed_image_path}")

    # Debug: Display the processed image
    cv2.imshow("Processed Image", thresh)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Extract text from the processed image
    file_text = pytesseract.image_to_string(Image.open(processed_image_path))
    print(f"Extracted Text: {file_text}")

    # Save the extracted text to a file
    text_file_path = os.path.join(output_dir, "extracted_text.txt")
    with open(text_file_path, "w", encoding="utf-8") as f:
        f.write(file_text)
    
    print(f"Text extraction complete and saved to: {text_file_path}")

# Define the path to the input image and output directory
image_path = r"set10\sample.jpg"
output_dir = "set10"

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Call the function to extract text from the image
extract_text_from_image(image_path, output_dir)
