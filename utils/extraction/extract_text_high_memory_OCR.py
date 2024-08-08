import cv2
import numpy as np
import pytesseract
from pdf2image import convert_from_path
import logging

logging.basicConfig(level=logging.INFO)

def extract_text_high_memory_OCR(pdf_path):
    """Extracts text data from a PDF file using OpenCV and Tesseract.

    Args:
        pdf_path: Path to the PDF file.

    Returns:
        A list of strings containing the extracted text data from each page.
    """
    try:
        pages = convert_from_path(pdf_path, 500)
        text_data = []
        for page_num, page in enumerate(pages):
            gray = cv2.cvtColor(np.array(page), cv2.COLOR_RGB2GRAY)
            thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
            text = pytesseract.image_to_string(thresh)
            text_data.append(text)
        return text_data
    except Exception as e:
        print(f"Error extracting text from {pdf_path}: {e}")
        return []
