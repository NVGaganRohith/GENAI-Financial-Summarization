import docx

# Function to read text from a .docx file
def read_docx_file(file_path):
    """
    Reads text from a .docx file.

    Args:
        file_path (str): The path to the .docx file to be read.

    Returns:
        str: The text content of the .docx file.

    Raises:
        FileNotFoundError: If the .docx file does not exist at the given path.
        IOError: If there is an error reading the .docx file.
    """
    try:
        doc = docx.Document(file_path)
        full_text = []
        for para in doc.paragraphs:
            full_text.append(para.text)
        return '\n'.join(full_text)
    except FileNotFoundError as e:
        raise FileNotFoundError(f"File not found: {file_path}") from e
    except IOError as e:
        raise IOError(f"Error reading the file: {file_path}") from e

