from file_loader import extract_text_from_pdf
from chunker import chunk_text

text = extract_text_from_pdf("test PDF.pdf")
chunks = chunk_text(text, chunk_size=300, overlap=50)

print(f"✅ Created {len(chunks)} chunks")
print("--- First chunk ---")
print(chunks[0])
