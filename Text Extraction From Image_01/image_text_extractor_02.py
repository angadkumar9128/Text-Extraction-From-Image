# Importing all required libraries
import os
import cv2
from PIL import Image
import pytesseract

# Set the Tesseract executable path if not in PATH
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

# Function to process an image and extract text
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
    processed_image_path = os.path.join(output_dir, f"{os.path.basename(image_path)}_processed.png")
    cv2.imwrite(processed_image_path, thresh)
    print(f"Processed image saved to: {processed_image_path}")

    # Extract text from the processed image
    file_text = pytesseract.image_to_string(Image.open(processed_image_path))
    print(f"Extracted Text from {image_path}: {file_text}")

    # Save the extracted text to a file
    text_file_path = os.path.join(output_dir, f"{os.path.basename(image_path)}_extracted.txt")
    with open(text_file_path, "w", encoding="utf-8") as f:
        f.write(file_text)
    
    print(f"Text extraction complete and saved to: {text_file_path}")

# Define the directory containing the images and the output directory
input_dir = "set10"
output_dir = "set10_output"

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Loop through all files in the input directory
for filename in os.listdir(input_dir):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        image_path = os.path.join(input_dir, filename)
        extract_text_from_image(image_path, output_dir)
