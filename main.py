import glob
import os
import warnings

# Configuration
from utils.config.set_path_for_tesseract_and_poppler import set_paths
from utils.config.set_openai_api_key import set_openai_api_key

# Extraction
from utils.extraction.extract_text_high_memory_OCR import extract_text_high_memory_OCR
from utils.extraction.extract_text_low_memory import extract_text_low_memory
from utils.extraction.extract_from_any_file import read_text_file

# Processing
from utils.processing.text_read_and_write import save_text_to_file
from utils.processing.process_text import process_pdf_texts

# Embeddings
from utils.embeddings.create_db_and_store_embedding import store_embeddings_openai
from utils.embeddings.generate_dbname import generate_dbname

# Analysis
from utils.analysis.generate_2_page_summary import analyze_with_llm_openai
from utils.analysis.generate_1_page_summary import summarize_text

# I/O
from utils.docx_io.save_analysis_to_docx import save_text_to_docx
from utils.docx_io.read_from_docx import read_docx_file


warnings.filterwarnings("ignore")

def main():
    # Set paths for local installations
    poppler_path = r".\utils\poppler-24.02.0\Library\bin"
    tesseract_path = r".\utils\TesseractOCR\tesseract.exe"
    set_paths(poppler_path, tesseract_path)

    # Check if the user wants to skip extraction and read from file
    while True:
        skip_extraction = input("Do you want to skip extraction from PDF and read directly from a file(txt/docx)? (yes/no): ").strip().lower()
        if skip_extraction in ['yes', 'no']:
            break
        else:
            print("Invalid input, please enter 'yes' or 'no'.")

    if skip_extraction == 'yes':
        while True:
            file_type = input("Enter the file type (txt or docx): ").strip().lower()
            if file_type in ['txt', 'docx']:
                break
            else:
                print("Invalid input, please enter 'txt' or 'docx'.")

        while True:
            file_path = input(f"Enter the path to the {file_type} file (ex: Output Files/output.{file_type}): ").strip()
            if os.path.isfile(file_path):
                all_text_data = read_text_file(file_path, file_type)
                print(f"Loaded text from '{file_path}'.")
                break
            else:
                print("File not found. Please enter a valid path.")
    else:
        # Prompt user for extraction method
        while True:
            print("Select the extraction method for processing the PDFs:")
            print('---------------------------------------------------------------------------------------------------')
            print("1. Low Memory Extraction: Suitable for low specification machines.")
            print("2. High Memory Extraction: Suitable for machines with higher memory. \n(Note: High Memory Extraction requires 16+ GB RAM & uses OCR and typically takes around 30 mins or more)")
            print('---------------------------------------------------------------------------------------------------')
            user_input = input("Choose your method:\n'1' for Low Memory Extraction(Fast and Less Accurate)\n'2' for High Memory Extraction(Slow and More Accurate)\nYour Choice: ").strip()
            if user_input in ['1', '2']:
                break
            else:
                print("Invalid input, please enter '1' or '2'.")

        print('---------------------------------------------------------------------------------------------------')
        print('Note:')
        print('1. Make sure your input file folder has reports belonging to only a single company.\n2. If this is not your first time running the code, make sure you are not having any residual files in the input files folder.\n3. Make sure your input file folder is in the same directory as the main script.')
        print('---------------------------------------------------------------------------------------------------')
        input_directory = input("Enter the folder name containing the input PDF files: ").strip()
        while not os.path.isdir(input_directory):
            print("Folder not found. Please enter a valid folder name containing input PDF files.")
            input_directory = input("Enter the folder name containing the input PDF files: ").strip()

        pdf_paths = glob.glob(f'{input_directory}/*.pdf')

        all_text_data = []
        if user_input == '2':
            print("You selected High Memory Extraction.")
            for pdf_path in pdf_paths:
                all_text_data.extend(extract_text_high_memory_OCR(pdf_path))
            all_text_data = "\n\n".join(all_text_data)
        else:
            print("You selected Low Memory Extraction.")
            all_text_data=""
            for pdf_path in pdf_paths:
                all_text_data+=(extract_text_low_memory(pdf_path))

        # Save the extracted text to a file if the user chose to do so
        save_text_to_file(all_text_data, 'Output Files/output.txt')
        print("Extracted text will saved to 'Output Files/output.txt'.")

    # Chunking the text data into documents for further processing
    chunk_size = 3000  # Changing these parameters will greatly affect the output
    chunk_overlap = 200  # Changing these parameters will greatly affect the output
    chunks = process_pdf_texts(all_text_data, chunk_size, chunk_overlap)

    # Checking to see if OpenAI API key is set up correctly
    set_openai_api_key()

    # Create a persistent db for each respective company
    # document_db_directory = generate_dbname()
    document_db_directory = input("Enter the name of company you are analyzing: ")

    # Store embeddings
    while True:
        replace = input("Do you want to replace the Knowledge Base contents if it exists? (yes/no): ").strip().lower()
        if replace in ["yes", "no"]:
            replace = replace == "yes"
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
    directory_creation_success_flag = store_embeddings_openai(chunks, document_db_directory,replace)

    if directory_creation_success_flag:
        print(f"Successfully created and stored embeddings for {document_db_directory}.")
    else:
        print("Error storing embeddings. Please restart the IDE and try again.")
        exit()

    # Perform LLM-based analysis
    analysis = analyze_with_llm_openai(document_db_directory)
    print('---------------------------------------------------------------------------------------------------')
    print("2 Page Summary:")
    print(analysis)
    print('---------------------------------------------------------------------------------------------------')
    save_text_to_docx(analysis, "Output Files/2 Page Summary.docx")

    # File paths
    input_file_path_2page = "Output Files/2 Page Summary.docx"
    output_file_path_1page = "Output Files/1 Page Summary.docx"

    # Step 1: Read the text from the 2-page .docx file
    text_2page = read_docx_file(input_file_path_2page)

    # Step 2: Summarize the text to 300-400 words (approx. 1-page)
    condensed_summary_1page = summarize_text(text_2page)

    # Step 3: Write the summarized text to the 1-page output .docx file
    save_text_to_docx(condensed_summary_1page, output_file_path_1page)
    print("1 Page Summary:")
    print(condensed_summary_1page)
    print('---------------------------------------------------------------------------------------------------')
    print("\nBoth 1 and 2 page summaries have been generated. You can find them with the names 1 Page Summary.docx & 2 Page Summary.docx in the same directory.")

if __name__ == "__main__":
    main()
 
