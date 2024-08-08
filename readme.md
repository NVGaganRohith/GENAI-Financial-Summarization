
# Project Setup and Troubleshooting Guide

## Requirements
- Requires Python 3.11.x
- Works on Windows/Linux/MacOS
- Must have installed TesseractOCR and Poppler and set in path
- Works with any IDE (Recommended VS Code)

For detailed instructions refer below.

*Note: For troubleshooting refer to [Troubleshooting Tips](#troubleshooting-tips).*
 

## Steps to Follow

### [Step 1](#step-1-opening-command-prompt) Open Command Prompt

### [Step 2](#step-2-creating-virtual-environment) Run the following commands (Optional/Recommended)

#### Installation and Environment creation:

**For Mac:**
```sh
brew install python@3.11
python3.11 -m venv <EnvironmentName>
source <EnvironmentName>/bin/activate
```

**For Windows:**
```sh
python -m venv <EnvironmentName>
.\<Environment Name>\Scripts\Activate
```

**For Linux:**
```sh
sudo apt-get install python3.11
python3.11 -m venv <Environmentname>
source <EnvironmentName>/bin/activate
```

### [Step 3](#step-3-moving-files-to-environment-folder) Once the env is created and activated, move all the files in the folder to newly created folder (named as <environment name>).

### [Step 4](#step-4-then-move-to-the-new-created-folder)
Then move to the new created folder:
```sh
cd <Environment Name>
```

*Note: If you haven't created a virtual environment, make sure your folder hierarchy is the same as below:*
```plaintext
<Your Project Directory>/
│
├── README.md
├── requirements.txt
├── main.py
│
├── utils/
│   ├── config/
│   │   ├── set_openai_api_key.py
│   │   └── set_path_for_tesseract_and_poppler.py
│   │
│   ├── extraction/
│   │   ├── extract_from_any_file.py
│   │   ├── extract_text_high_memory_OCR.py
│   │   └── extract_text_low_memory.py
│   │
│   ├── processing/
│   │   ├── process_text.py
│   │   ├── split_and_chunk_text.py
│   │   └── text_read_and_write.py
│   │
│   ├── embeddings/
│   │   ├── create_db_and_store_embedding.py
│   │   └── generate_dbname.py
│   │
│   ├── analysis/
│   │   ├── generate_1_page_summary.py
│   │   └── llm_analysis.py
│   │
│   ├── docx_io/
│   │   ├── read_and_write_from_docx.py
│   │   └── save_analysis_to_docx.py
│   │
│   ├── TesseractOCR/
│   └── poppler-24.02.0/
```

### [Step 5](#step-5-installing-pytesseract-and-poppler-for-your-system)
Installing pytesseract and poppler for your system (the installation steps differ for each OS).

**For Windows:**
You can directly download the files from the below link and extract them in the utils folder inside the environment folder.
- [Download Files](https://drive.google.com/file/d/1yyTOfiY3mh--WA3W2GKmt1-GWu5LeBuj/view?usp=drive_link)

Or

You can manually go to GitHub and install them.
- TesseractOCR: [TesseractOCR GitHub](https://github.com/UB-Mannheim/tesseract/wiki) (Download latest version (5.4 preferred))
- Poppler: [Poppler GitHub](https://github.com/oschwartz10612/poppler-windows/releases) (Download version 23 or later)

**For MacOS:**
```sh
brew install tesseract
brew install poppler
```

**For Linux:**
```sh
sudo apt update
sudo apt install tesseract-ocr poppler-utils
```

*Note: In MacOS and Linux, the installations will automatically set in path. If you use Binary Installer in Windows it will do the same.*

### [Step 6](#step-6-if-you-are-using-a-python-version-equal-or-above-311)
If you are using a python version equal or above 3.11 then run this:
```sh
pip install -r requirements.txt
```

*Note: If this is giving version error then run the below command and install manually.*
```sh
pip install opencv-python numpy pytesseract pdf2image langchain torch chromadb langchain_community openai python-docx tiktoken PyMuPdf
```

### [Step 7](#step-7-create-an-input-folder-folder_name)
Create an input folder <Folder_Name>, and add all the PDFs that you want to summarize.
(Make sure to create the folder in the same directory as the main script)

### [Step 8](#step-8-create-a-folder-named-output-files)
Create a folder named "Output Files", if it doesn't exist already.

### [Step 9](#step-9-once-everything-is-setup-correctly-run-the-below-command)
Once everything is set up correctly, run the below command:
```sh
python main.py
```
Provide inputs according to your requirements.

*Note: If you are creating a virtual environment, make sure you check your pwd and you are in the same directory as the main script, and the virtual environment is activated.*

## [Troubleshooting Tips](#troubleshooting-tips)

1) **If you are using python 3.12.x, run these commands-**
    ```sh
    pip uninstall chromadb
    pip install chromadb==0.5.3
    ```

2) **Make sure you are having Input Files and Output Files folder inside your current directory before running main.py.**

3) **Environment Activation:**
    Make sure your virtual environment is activated before installing dependencies or running scripts. You should see the environment name in your terminal prompt.

4) **Virtual Environment Not Found:**
    If you get an error that the virtual environment cannot be found, ensure you created it correctly and are providing the correct path.

5) **Environment Activation Errors:**
    - **Windows:** Ensure you are running the command prompt as an administrator if you face permission issues.
    - **MacOS/Linux:** Use `source <EnvironmentName>/bin/activate` and ensure you have the correct permissions.

6) **Creating Input Folder:**
    - **Permission Issues:** Ensure you have the necessary permissions to create folders and add files. Use `mkdir <Folder_Name>` to create the folder.
    - **Directory Structure:** Ensure the folder is created in the same directory as the main script.

7) **Running the Script:**
    - **Script Not Running:** Ensure you are in the correct directory where main.py is located. Run `pwd` to check your current directory.
    - **Python Version Errors:** Make sure you are using Python 3.11.x. If not, update your Python version.
    - **File Not Found Errors:** Ensure all required files and directories are in place and correctly named.
    - **Permission Issues:** Run the terminal as an administrator (Windows) or use `sudo` (Linux/MacOS) if you face permission issues.

8) **Common Errors and Fixes:**
    - **Module Not Found:** If you encounter "ModuleNotFoundError", ensure all dependencies are installed and your virtual environment is activated.
    - **Path Issues:** Double-check the PATH settings for TesseractOCR and Poppler. Verify with `echo $PATH` (Linux/MacOS) or `echo %PATH%` (Windows).
    - **Permission Denied:** Ensure you have the necessary permissions. Run the terminal as an administrator or use `sudo` for commands that require elevated privileges.



For further support, contact: Nadella.VenkataGaganRohith@genpact.com