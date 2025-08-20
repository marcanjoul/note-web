import warnings
warnings.simplefilter("ignore")


import os
os.environ["TOKENIZERS_PARALLELISM"] = "false"

import json
from embedder import get_embedding
from llm_answerer import answer_with_llama
import numpy as np


def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def search_index(query: str, k: int = 3) -> list:
    # Load the saved index
    with open("embeddings_index.json", "r") as json_file:
        index = json.load(json_file)

    # Get embedding for the query
    query_embedding = get_embedding(query)

    results = []
    for item in index:
        item_embedding = np.array(item["embedding"])
        similarity = cosine_similarity(query_embedding, item_embedding)
        results.append({
            "score": similarity,
            "text": item["text"]
        })

    # Sort results and return top k
    results.sort(key=lambda x: x["score"], reverse=True)
    return results[:k]

# Test the function right here:
if __name__ == "__main__":
    history = []

    while True:
        query = input("\n🧠 Ask a question (or type 'exit' to quit): ").strip()
        if query.lower() in {"exit", "quit"}:
            break

        top_chunks = search_index(query)
        answer = answer_with_llama(query, top_chunks, history)

        # Show the LLM's answer
        print("\n🤖 LLaMA 3 says:\n")
        print(answer)

        # Add this Q&A to history
        history.append({
            "question": query,
            "answer": answer
        })

#incase we wanted the suitable chunks to be displayed!
#    for result in top_chunks:
#        print(result["score"], result["text"])
#   response = answer_with_llama(query, top_chunks)
#   print("\n🤖 LLaMA 3 says:\n")
#   print(response)