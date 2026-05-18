import pytesseract
from PIL import Image

# File paths of the uploaded images
file_paths = [
    r"C:\Users\KIIT0001\OneDrive\Desktop\syll\os sylla.jpg",
    r"C:\Users\KIIT0001\OneDrive\Desktop\syll\itc sylls.jpg",
    r"C:\Users\KIIT0001\OneDrive\Desktop\syll\eco sylla.jpg",
    r"C:\Users\KIIT0001\OneDrive\Desktop\syll\dm sylla.jpg",
    r"C:\Users\KIIT0001\OneDrive\Desktop\syll\dbms syulla.jpg"
]

# Extract text from each image
extracted_texts = {}
for path in file_paths:
    image = Image.open(path)
    text = pytesseract.image_to_string(image)
    extracted_texts[path] = text

# Return the extracted text
extracted_texts
