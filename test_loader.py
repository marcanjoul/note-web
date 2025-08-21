# test_loader.py

from files_loader import extract_text_from_pdf

file_path = "Test PDF.pdf"  # Change this if your file is named differently
text = extract_text_from_pdf(file_path)

print("Extracted text:")
print(text)
