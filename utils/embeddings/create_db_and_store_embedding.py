# import os
# from langchain_community.embeddings import OpenAIEmbeddings
# from langchain_community.vectorstores import Chroma
# import openai
# import logging

# logging.basicConfig(level=logging.INFO)

# def store_embeddings_openai(chunks, document_db_directory):
#     """Stores embeddings of document chunks into a Chroma vector database using OpenAI embeddings.

#     Args:
#         chunks (list): List of document chunks to be embedded.
#         document_db_directory (str): Directory where the Chroma vector database is persisted.

#     Returns:
#         bool: True if embeddings are stored successfully, False otherwise.
#     """
#     try:
#         # Initialize OpenAI API
#         openai.api_key = os.getenv('OPENAI_API_KEY')

#         if not openai.api_key:
#             raise ValueError("OpenAI API key not found in environment variables.")

#         # Define maximum batch size
#         max_batch_size = 166

#         # Initialize OpenAI embeddings
#         embeddings = OpenAIEmbeddings()

#         # Process chunks in batches
#         for i in range(0, len(chunks), max_batch_size):
#             batch_chunks = chunks[i:i + max_batch_size]

#             # Store embeddings in the Chroma vector database for each batch
#             Chroma.from_documents(documents=batch_chunks, embedding=embeddings, persist_directory=document_db_directory)

#         # Persist the changes to the database
#         chroma_instance = Chroma(persist_directory=document_db_directory)
#         chroma_instance.persist()

#         logging.info(f"Embeddings stored successfully in {document_db_directory}.")
#         return True

#     except ValueError as ve:
#         logging.error(f"ValueError: {ve}")
#     except Exception as e:
#         logging.error(f"Error storing embeddings with OpenAI: {e}")

#     return False


import os
import shutil
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
import openai
import logging

logging.basicConfig(level=logging.INFO)

def store_embeddings_openai(chunks, document_db_directory, replace_existing=True):
    """Stores embeddings of document chunks into a Chroma vector database using OpenAI embeddings.

    Args:
        chunks (list): List of document chunks to be embedded.
        document_db_directory (str): Directory where the Chroma vector database is persisted.
        replace_existing (bool): Whether to replace existing contents if the directory exists.

    Returns:
        bool: True if embeddings are stored successfully, False otherwise.
    """
    try:
        # Initialize OpenAI API
        openai.api_key = os.getenv('OPENAI_API_KEY')

        if not openai.api_key:
            raise ValueError("OpenAI API key not found in environment variables.")

        # Check if the directory exists
        if os.path.exists(document_db_directory):
            if replace_existing:
                # Remove existing contents
                shutil.rmtree(document_db_directory)
                os.makedirs(document_db_directory)
                logging.info(f"Existing directory {document_db_directory} cleared and recreated.")
            else:
                logging.info(f"Using existing directory {document_db_directory} without clearing.")
        else:
            os.makedirs(document_db_directory)
            logging.info(f"Directory {document_db_directory} created.")

        # Define maximum batch size
        max_batch_size = 166

        # Initialize OpenAI embeddings
        embeddings = OpenAIEmbeddings()

        # Process chunks in batches
        for i in range(0, len(chunks), max_batch_size):
            batch_chunks = chunks[i:i + max_batch_size]

            # Store embeddings in the Chroma vector database for each batch
            Chroma.from_documents(documents=batch_chunks, embedding=embeddings, persist_directory=document_db_directory)

        # Persist the changes to the database
        chroma_instance = Chroma(persist_directory=document_db_directory)
        chroma_instance.persist()

        logging.info(f"Embeddings stored successfully in {document_db_directory}.")
        return True

    except ValueError as ve:
        logging.error(f"ValueError: {ve}")
    except Exception as e:
        logging.error(f"Error storing embeddings with OpenAI: {e}")

    return False

