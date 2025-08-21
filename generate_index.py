import os  # For interacting with the operating system, e.g., listing files and joining paths.
import json  # For saving the final index as a JSON file.
from files_loader import extract_text_from_file  # Function to extract text from various file types.
from chunker import chunk_text  # Function to split large texts into smaller, manageable chunks.
from embedder import get_embedding  # Function to generate embeddings for text chunks.

index = []  # Initialize an empty list to store the final index of text chunks and their embeddings.

# 1. Path to your folder (can include PDFs, .docx, .pptx, etc.)
folder_path = "test files"  # Specify the folder containing files to be indexed. Change as needed.
file_names = os.listdir(folder_path)  # List all files in the specified folder.

# 2. Process each file
for file_name in file_names:
    file_path = os.path.join(folder_path, file_name)  # Get the full path to the current file.
    print(f" Processing: {file_name}")  # Informative print statement for tracking progress.

    text = extract_text_from_file(file_path)  # Extract all text from the current file.

    if not text.strip():
        # If the extracted text is empty or the file type is unsupported, skip this file.
        print(f"Skipped (empty or unsupported): {file_name}")
        continue

    chunks = chunk_text(text)  # Split the extracted text into smaller chunks for embedding.
    print(f"🧩 {len(chunks)} chunks created")  # Print the number of chunks created for this file.

    for chunk in chunks:
        embedding = get_embedding(chunk)  # Generate an embedding for the current chunk.
        if embedding:
            # If embedding is successfully generated, add it to the index.
            index.append({
                "text": chunk,  # Store the chunk's text.
                "embedding": embedding  # Store the corresponding embedding vector.
            })

# 3. Save the final index
with open("embeddings_index.json", "w") as f:
    # Write the index (list of chunk dictionaries) to a JSON file for later use.
    json.dump(index, f)

print("Indexing complete. Saved to embeddings_index.json")  #
