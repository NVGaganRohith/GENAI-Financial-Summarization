from utils.processing.text_read_and_write import load_text_from_file
from docx import Document

def read_text_file(file_path, file_type):
    """
    Reads text from a .txt or .docx file.

    Args:
        file_path (str): Path to the file.
        file_type (str): Type of the file ('txt' or 'docx').

    Returns:
        str: Content of the file.
    """
    if file_type == 'txt':
        return load_text_from_file(file_path)
    elif file_type == 'docx':
        doc = Document(file_path)
        full_text = []
        for para in doc.paragraphs:
            full_text.append(para.text)
        return '\n'.join(full_text)
    else:
        raise ValueError("Unsupported file type. Please use 'txt' or 'docx'.")
