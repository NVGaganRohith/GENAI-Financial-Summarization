from utils.processing.split_and_chunk_text import chunk_text
import logging

logging.basicConfig(level=logging.INFO)

def save_text_to_file(text, file_path):
    """
    Saves the given text data to a file with double newline separation.

    Args:
        text (str): The text data to be saved as a single string.
        file_path (str): The path to the file where the text will be saved.

    Raises:
        IOError: If there is an error saving the text to the file.
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(text)  # No change if you are using single string with newlines.
        logging.info(f"Text successfully saved to {file_path}.")
    except IOError as e:
        logging.error(f"Error saving text to file: {e}")
        raise



def load_text_from_file(file_path):
    """
    Loads text data from a file, splitting it by double newline separation.

    Args:
        file_path (str): The path to the file from which the text will be loaded.

    Returns:
        list of str: The loaded text data split by double newline.

    Raises:
        IOError: If there is an error loading the text from the file.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text_data = file.read().split("\n\n")
        logging.info(f"Text successfully loaded from {file_path}.")
        return text_data
    except IOError as e:
        logging.error(f"Error loading text from file: {e}")
        raise


