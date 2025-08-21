# chunker.py
# This module provides a utility function to split long text into smaller, overlapping chunks.
# Useful for processing large documents in NLP tasks, summarization, or when sending data to APIs with size limits.

def chunk_text(text, chunk_size=500, overlap=50):
    """
    Splits long text into overlapping chunks.

    Args:
        text (str): The full text to split.
        chunk_size (int): Max number of characters per chunk. Default is 500.
        overlap (int): Number of characters that overlap between chunks. Default is 50.

    Returns:
        List[str]: A list of text chunks, each with a maximum length of 'chunk_size' characters.
    """
    chunks = []  # List to store resulting text chunks
    start = 0    # Start index for the current chunk

    # Continue splitting until the start index reaches the end of the text
    while start < len(text):
        end = start + chunk_size  # Calculate the end index for the current chunk

        # Extract the chunk from the text using slicing.
        # Slicing will not raise an error if 'end' exceeds the length of 'text';
        # it will simply return up to the end of the string.
        chunk = text[start:end]

        # Append the current chunk to the list of chunks.
        # Each chunk will have a maximum length of 'chunk_size' characters.
        chunks.append(chunk)

        # Move the start index forward by (chunk_size - overlap).
        # This ensures that each new chunk starts 'chunk_size - overlap' characters
        # after the previous chunk's start, creating an overlap of 'overlap' characters
        # between consecutive chunks.
        start += chunk_size - overlap

    # Return the list of text chunks.
    # The last chunk may be shorter than 'chunk_size' if the text length is not a multiple of
    # (chunk_size - overlap), but it will still be a valid chunk.
    return chunks

# Example usage:
# text = "Your very long text goes here..."
# chunks = chunk_text(text, chunk_size=500, overlap=50)
# print(chunks)  # Prints the list of overlapping chunks

# Notes:
# - Overlapping chunks are useful for preserving context between splits, especially in NLP tasks.
# - Adjust 'chunk_size' and 'overlap' based on your application's requirements and API limits.
# - This function operates on character count, not word count. For word-based chunking, modify the
#   logic to split on spaces or use text.split().
# - If 'overlap' is set to 0, chunks will be non-overlapping.
# - If 'chunk_size' is less than or equal to 'overlap', the function will create highly redundant chunks.
# - The function does not perform any preprocessing (e.g., removing whitespace or punctuation).
# - For very large texts, consider memory usage as all chunks are stored in the 'chunks' list.
