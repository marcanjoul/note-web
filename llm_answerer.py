import subprocess
import warnings
from urllib3.exceptions import NotOpenSSLWarning  # 👈 key fix
warnings.filterwarnings("ignore", category=NotOpenSSLWarning)

import os
os.environ["TOKENIZERS_PARALLELISM"] = "false"

def build_prompt(query, top_chunks, history=None):
    combined_chunks = ""
    for chunk in top_chunks:
        combined_chunks += chunk["text"] + "\n"

    history_prompt = ""
    if history:
        for pair in history:
            history_prompt += f"Q: {pair['question']}\nA: {pair['answer']}\n"

    return (
        "You are trained to answer academic questions from imported doc(s), "
        "be clear, concise, a little casual, and helpful when answering the following question(s)!\n"
        f"Context:\n{combined_chunks}\n"
        f"Question: {query}"
    )

def answer_with_llama(query, top_chunks, history=None):
    prompt = build_prompt(query, top_chunks, history)

    result = subprocess.run(
        ["ollama", "run", "llama3:instruct"],
        input=prompt,
        text=True,
        capture_output=True
    )

    return result.stdout.strip()
