import os
import json
from files_loader import extract_text_from_file
from chunker import chunk_text
from embedder import get_embedding

index = []

# 1. Path to your folder (can include PDFs, .docx, .pptx, etc.)
folder_path = "test files"  # rename to match your actual folder
file_names = os.listdir(folder_path)

# 2. Process each file
for file_name in file_names:
    file_path = os.path.join(folder_path, file_name)
    print(f"📄 Processing: {file_name}")

    text = extract_text_from_file(file_path)

    if not text.strip():
        print(f"⚠️ Skipped (empty or unsupported): {file_name}")
        continue

    chunks = chunk_text(text)
    print(f"🧩 {len(chunks)} chunks created")

    for chunk in chunks:
        embedding = get_embedding(chunk)
        if embedding:
            index.append({
                "text": chunk,
                "embedding": embedding
            })

# 3. Save the final index
with open("embeddings_index.json", "w") as f:
    json.dump(index, f)

print("✅ Indexing complete. Saved to embeddings_index.json")
