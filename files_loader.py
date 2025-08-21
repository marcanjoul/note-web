import os
import fitz  # PyMuPDF, used to read and process PDFs
from docx import Document
from openpyxl import load_workbook
from pptx import Presentation

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

def extract_text_from_multiple_pdfs(file_paths):
    """
    Extracts and combines text from multiple PDF files.

    Args:
        file_paths (List[str]): A list of paths to PDF files.

    Returns:
        str: Combined text from all PDFs.
    """
    combined_text = ""
    for path in file_paths:
        print(f" Extracting: {path}")
        combined_text += extract_text_from_pdf(path) + "\n"
    return combined_text

def extract_text_from_docx(file_path):
    """
    Opens a word doc and extracts all the text from every page.
    
    Args:
        file_path (str): The path to the docx file.
    
    Returns:
        str: The full extracted text from the docx.
    """
    text = ""  # Start with an empty string to collect text

    try:
        doc = Document(file_path)
        for para in doc.paragraphs:
            text += para.text + "\n"
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
    return text


def extract_text_from_xlsx(file_path):
    text = ""
    try:
        wb = load_workbook(file_path)
        for sheet in wb.worksheets:
            for row in sheet.iter_rows(values_only=True):
                for cell in row:
                    if cell:
                        text += str(cell) + " "
                text += "\n"
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
    return text


def extract_text_from_pptx(file_path):
    text = ""
    try:
        prs = Presentation(file_path)
        for slide in prs.slides:
            for shape in slide.shapes:
                if hasattr(shape, "text"):
                    text += shape.text + "\n"
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
    return text

def extract_text_from_file(file_path):
    ext = os.path.splitext(file_path)[1].lower()

    if ext == ".pdf":
        return extract_text_from_pdf(file_path)
    elif ext == ".docx":
        return extract_text_from_docx(file_path)
    elif ext == ".xlsx":
        return extract_text_from_xlsx(file_path)
    elif ext == ".pptx":
        return extract_text_from_pptx(file_path)
    else:
        print(f"Unsupported file type: {ext}")
        return ""