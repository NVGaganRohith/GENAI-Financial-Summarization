from utils.processing.split_and_chunk_text import chunk_text
import logging

logging.basicConfig(level=logging.INFO)

def process_pdf_texts(pdf_texts, chunk_size, chunk_overlap):
    """
    Processes the given PDF texts by chunking them into smaller segments.

    Args:
        pdf_texts (list of str): The text data extracted from PDFs.
        chunk_size (int): The maximum size of each chunk.
        chunk_overlap (int): The overlap size between consecutive chunks.

    Returns:
        list of Document: A list of Document objects containing the chunked text.

    Raises:
        ValueError: If the text cannot be processed due to invalid parameters.
        Exception: If there is an unexpected error during the processing.
    """
    try:
        documents = chunk_text(pdf_texts, chunk_size, chunk_overlap)
        logging.info(f"Text processed into {len(documents)} documents.")
        return documents
    except ValueError as ve:
        logging.error(f"ValueError in processing PDF texts: {ve}")
        return []
    except Exception as e:
        logging.error(f"Unexpected error in processing PDF texts: {e}")
        return []
