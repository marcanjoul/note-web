# embedder.py

import os
from openai import OpenAI
from dotenv import load_dotenv

# Load .env file and get API key
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_embedding(text, model="text-embedding-3-small"):
    """
    Returns the embedding vector for a given text using OpenAI's v1 client.
    """
    try:
        response = client.embeddings.create(
            input=text,
            model=model
        )
        return response.data[0].embedding
    except Exception as e:
        print(f"Failed to get embedding: {e}")
        return None
