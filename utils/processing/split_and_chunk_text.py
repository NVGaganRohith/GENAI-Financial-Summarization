from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
import logging

logging.basicConfig(level=logging.INFO)

def split_text(combined_text, chunk_size, chunk_overlap):
    """
    Splits the combined text into chunks using RecursiveCharacterTextSplitter.

    Args:
        combined_text (str): The combined text to be split.
        chunk_size (int): The maximum size of each chunk.
        chunk_overlap (int): The overlap size between consecutive chunks.

    Returns:
        list of str: A list of chunked text.
    
    Raises:
        ValueError: If the text cannot be split due to invalid parameters.
    """
    try:
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            length_function=len
        )
        return text_splitter.split_text(combined_text)
    except ValueError as ve:
        logging.error(f"ValueError in splitting text: {ve}")
        raise
    except Exception as e:
        logging.error(f"Unexpected error in splitting text: {e}")
        raise


def chunk_text(text_data, chunk_size, chunk_overlap):
    """
    Chunks the given text data into smaller segments using RecursiveCharacterTextSplitter.

    Args:
        text_data (list of str): The text data to be chunked.
        chunk_size (int): The maximum size of each chunk.
        chunk_overlap (int): The overlap size between consecutive chunks.

    Returns:
        list of Document: A list of Document objects containing the chunked text.

    Raises:
        ValueError: If the text cannot be chunked due to invalid parameters.
        Exception: If there is an unexpected error during the chunking process.
    """
    try:
        combined_text = "\n\n".join(text_data)  # Join the list of strings into a single string
        chunks = split_text(combined_text, chunk_size, chunk_overlap)
        documents = [Document(page_content=chunk) for chunk in chunks]
        return documents
    except ValueError as ve:
        logging.error(f"ValueError in chunking text: {ve}")
        return []
    except Exception as e:
        logging.error(f"Unexpected error in chunking text: {e}")
        return []
