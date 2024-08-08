import fitz  # PyMuPDF
import logging

logging.basicConfig(level=logging.INFO)

def extract_text_low_memory(pdf_path):
    """
    Extracts text from each page of a PDF file using PyMuPDF.
    
    Args:
        pdf_path (str): Path to the PDF file.

    Returns:
        str: Extracted text from the PDF.
    """
    text = ""
    try:
        doc = fitz.open(pdf_path)
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            text += f'\n\nPage {page_num + 1}\n'
            text += page.get_text()
        doc.close()
    except fitz.FileDataError:
        logging.error(f"File data error while processing {pdf_path}. The file may be corrupted or invalid.")
    except fitz.FitzError:
        logging.error(f"Fitz error while processing {pdf_path}.")
    except Exception as e:
        logging.error(f"Unexpected error extracting text from {pdf_path}: {e}")
    return text
