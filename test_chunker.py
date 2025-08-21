from files_loader import extract_text_from_pdf  # Function to extract text from a PDF file.
from chunker import chunk_text  # Function to split text into chunks with optional overlap.

# Extract all text from the specified PDF file.
text = extract_text_from_pdf("test PDF.pdf")

# Split the extracted text into chunks of 300 characters, with 50 characters overlapping between chunks.
chunks = chunk_text(text, chunk_size=300, overlap=50)

# Print the total number of chunks created for verification.
print(f"Created {len(chunks)} chunks")

# Print a separator for clarity.
print("--- First chunk ---")

# Print the contents of the first chunk to inspect chunking
