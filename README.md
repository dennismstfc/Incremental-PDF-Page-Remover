# Incremental PDF Page Remover

This project, **Incremental PDF Page Remover**, provides a convenient web interface to detect and remove redundant incremental pages in PDF files. Pages that are at least 80% similar to their previous version are considered redundant and only the last version in any sequence of incremental pages is retained. 

## Getting Started
Install the required Python packages with:
```bash
pip install -r requirements.txt
```

### Important files
- `main.py`: Runs the Streamlit web app.

- `pdf_processor.py`: Contains the `PDFProcessor` class with the logic for identifying and removing redundant pages.
- `scripts/`: Directory where uploaded PDF files are saved temporarily for processing.

### How It Works
1. **File Upload**: Use the Streamlit web interface to upload a PDF file.
2. **Processing**: The uploaded PDF is processed to remove redundant pages based on a similarity threshold of 80%.
3. **Download**: Once processed, download the optimized PDF with all redundant pages removed.

## Usage

1. **Run the Streamlit app**:
   ```bash
   streamlit run main.py
   ```
2. **Upload PDF**: Drag and drop a PDF file into the file uploader.
3. **Process & Download**: Click the button to process the file and remove redundant pages. A download link will appear once processing is complete.

## Author
Made with ❤️ by [Dennis Mustafić](https://github.com/dennismstfc)
