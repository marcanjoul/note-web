# embedder.py (local version)

# Import the SentenceTransformer class from the sentence_transformers library.
# This library provides easy-to-use methods for generating sentence embeddings using transformer models.
from sentence_transformers import SentenceTransformer

# Load a pre-trained, lightweight transformer model for generating embeddings.
# 'all-MiniLM-L6-v2' is a small, fast model suitable for local use and quick inference.
model = SentenceTransformer('all-MiniLM-L6-v2')

def get_embedding(text):
    """
    Generate and return the embedding vector for a given input text using the loaded local model.

    Args:
        text (str): The input text string to be embedded.

    Returns:
        list or None: The embedding vector as a plain Python list if successful,
                      or None if an error occurs during embedding.
    """
    try:
        # Encode the input text to obtain its embedding vector.
        # The model.encode() method returns a numpy array representing the embedding.
        embedding = model.encode(text)
        # Convert the numpy array to a standard Python list for easier serialization and compatibility.
        return embedding.tolist()
    except Exception as e:
        # If any error occurs during encoding, print an error message and return None.
        print(f"Failed to get embedding: {e}")
        return None
