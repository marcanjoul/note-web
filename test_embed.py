from embedder import get_embedding  # Import the function to generate embeddings for text.

# Define a sample text string to embed.
text = "Stacks are Last-In-First-Out (LIFO)."

# Generate the embedding vector for the sample text using the local model.
embedding = get_embedding(text)

# Check if an embedding was successfully returned.
if embedding:
    # Print a confirmation message with the length of the embedding vector.
    print(f"✅ Got embedding of length {len(embedding)}")
    # Print the first 5 values of the embedding for inspection.
    print(embedding[:5])  # First 5 values
else:
    # Print a message if no embedding was returned (e.g., due to an error).
    print("No embedding returned")
