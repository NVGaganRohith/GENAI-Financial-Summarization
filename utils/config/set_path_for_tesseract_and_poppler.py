import pytesseract
import os
import logging

logging.basicConfig(level=logging.INFO)

def set_paths(poppler_path, tesseract_path):
    """Sets the paths for Poppler and Tesseract executables.

    Adds the Poppler path to the system PATH environment variable and sets the Tesseract executable path.

    Args:
        poppler_path (str): Path to the Poppler bin folder.
        tesseract_path (str): Path to the Tesseract executable(tesseract.exe).
    """
    try:
        os.environ['PATH'] = poppler_path + os.pathsep + os.environ['PATH']
        pytesseract.pytesseract.tesseract_cmd = tesseract_path
        logging.info(f"Paths set successfully: Poppler path - {poppler_path}, Tesseract path - {tesseract_path}")
    except Exception as e:
        logging.error(f"Error setting paths: {e}")
