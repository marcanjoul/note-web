import json                      # to save the index as a .json file
from embedder import get_embedding  # to use your embedding function
from chunker import chunk_text
from file_loader import extract_text_from_multiple_pdfs 

# List of PDF files to process
pdf_files = ["PDFs/Mindset copy.pdf", "PDFs/Retention of Learning & Rehearsal copy.pdf"]  # Add your actual filenames here


pdf_files = [
    "PDFs/Mindset copy.pdf",
    "PDFs/Retention of Learning & Rehearsal copy.pdf"
]

text = extract_text_from_multiple_pdfs(pdf_files)

index = []
chunks = chunk_text(text)

print(f"🔍 Loaded {len(chunks)} chunks from the PDF.")

for chunk in chunks:
    embedding = get_embedding(chunk)
    if embedding:  # Only add to index if embedding was successful
        index.append({
            "text": chunk,
            "embedding": embedding
        })

# Save the index to a file
with open("embeddings_index.json", "w") as json_file:
    json.dump(index, json_file, indent=4)


