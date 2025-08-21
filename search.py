import warnings  # Used to suppress warning messages from libraries.
warnings.simplefilter("ignore")  # Ignore all warnings for cleaner output.

import os  # Used for environment variable management.
os.environ["TOKENIZERS_PARALLELISM"] = "false"  # Prevents parallelism warnings from tokenizer libraries.

import json  # For loading the embeddings index from a JSON file.
from embedder import get_embedding  # Function to generate embeddings for queries.
from llm_answerer import answer_with_llama  # Function to get answers from the LLM.
import numpy as np  # For numerical operations, especially vector math.

def cosine_similarity(a, b):
    """
    Computes the cosine similarity between two vectors.

    Args:
        a (np.ndarray): First vector.
        b (np.ndarray): Second vector.

    Returns:
        float: Cosine similarity score between a and b.
    """
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def search_index(query: str, k: int = 3) -> list:
    """
    Searches the embeddings index for the top-k most relevant text chunks to the query.

    Args:
        query (str): The user's search query.
        k (int): Number of top results to return.

    Returns:
        list: List of top-k dictionaries containing 'score' and 'text' for each chunk.
    """
    # Load the saved index of text chunks and their embeddings from disk.
    with open("embeddings_index.json", "r") as json_file:
        index = json.load(json_file)

    # Generate an embedding for the user's query using the same model as the index.
    query_embedding = get_embedding(query)

    results = []  # Will store similarity scores and corresponding text chunks.
    for item in index:
        item_embedding = np.array(item["embedding"])  # Convert stored embedding to numpy array.
        similarity = cosine_similarity(query_embedding, item_embedding)  # Compute similarity.
        results.append({
            "score": similarity,  # Similarity score between query and chunk.
            "text": item["text"]  # The chunk's text.
        })

    # Sort results by similarity score in descending order and return the top k.
    results.sort(key=lambda x: x["score"], reverse=True)
    return results[:k]

# If this script is run directly, start an interactive Q&A loop.
if __name__ == "__main__":
    history = []  # Stores previous Q&A pairs for conversational context.

    while True:
        # Prompt the user for a question.
        query = input("\n🧠 Ask a question (or type 'exit' to quit): ").strip()
        if query.lower() in {"exit", "quit"}:
            break  # Exit the loop if the user wants to quit.

        top_chunks = search_index(query)  # Find the most relevant chunks for the query.
        answer = answer_with_llama(query, top_chunks, history)  # Get an answer from the LLM.

        # Display the LLM's answer to the user.
        print("\n🤖 LLaMA 3 says:\n")
        print(answer)

        # Add this Q&A to history for context in future questions.
        history.append({
            "question": query,
            "answer": answer
        })

# If you want to display the top chunks and their scores for debugging or transparency,
# uncomment the following lines:
#    for result in top_chunks:
#        print(result["score"], result["text"])
#   response = answer_with_llama(query, top_chunks)
#   print("\n🤖 LLaMA 3 says:\n")
#