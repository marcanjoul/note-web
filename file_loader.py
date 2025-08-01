# file_loader.py

import fitz  # PyMuPDF, used to read and process PDFs

def extract_text_from_pdf(file_path):
    """
    Opens a PDF and extracts all the text from every page.
    
    Args:
        file_path (str): The path to the PDF file.
    
    Returns:
        str: The full extracted text from the PDF.
    """
    text = ""  # Start with an empty string to collect text

    try:
        with fitz.open(file_path) as doc:  # Open the PDF file safely
            for page in doc:  # Loop through each page
                text += page.get_text()  # Extract text and add to the running string
    except Exception as e:
        print(f" Error reading {file_path}: {e}")
    
    return text  # Return all the collected text

