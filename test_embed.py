from embedder import get_embedding

text = "Stacks are Last-In-First-Out (LIFO)."
embedding = get_embedding(text)

if embedding:
    print(f"✅ Got embedding of length {len(embedding)}")
    print(embedding[:5])  # First 5 values
else:
    print("No embedding returned")
