# embedder.py (local version)

from sentence_transformers import SentenceTransformer

# Load a small, fast local model
model = SentenceTransformer('all-MiniLM-L6-v2')

def get_embedding(text):
    """
    Returns the embedding vector for a given text using a local model.
    """
    try:
        embedding = model.encode(text)
        return embedding.tolist()  # Return as a plain list
    except Exception as e:
        print(f"Failed to get embedding: {e}")
        return None
