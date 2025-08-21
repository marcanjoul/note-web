# test_loader.py

# Import the function to extract text from a PDF file.
from files_loader import extract_text_from_pdf

# Specify the path to the PDF file to be tested.
file_path = "Test PDF.pdf"  # Change this if your file is named differently

# Extract all text from the specified PDF file using the extraction function.
text = extract_text_from_pdf(file_path)

# Print a header to indicate that extracted text will follow.
print("Extracted text:")

# Print the actual extracted text from the PDF for
