# chunker.py

def chunk_text(text, chunk_size=500, overlap=50):
    """
    Splits long text into overlapping chunks.

    Args:
        text (str): The full text to split.
        chunk_size (int): Max number of characters per chunk.
        overlap (int): Number of characters that overlap between chunks.

    Returns:
        List[str]: A list of text chunks.
    """
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start += chunk_size - overlap  # Move forward, keeping some overlap

    return chunks
