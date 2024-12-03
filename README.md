# Incremental PDF Page Remover

**Incremental PDF Page Remover** helps remove redundant pages in PDF files. Pages that are similar to the previous version (based on a similarity threshold) are considered redundant, and only the last version in any sequence is retained.

### New Feature: Adjustable Similarity Threshold
You can now adjust the similarity threshold using a slider, which can be set from **0% to 100%**. The default threshold is set to **90%**—if pages are more than 90% similar to the previous page, they will be removed.

### Important files
- `main.py`: Runs the Streamlit web app.
- `pdf_processor.py`: Contains the logic for removing redundant pages.
- `scripts/`: Directory where uploaded PDFs are temporarily stored.

### How It Works
1. **Upload PDF**: Use the Streamlit interface to upload a PDF.
2. **Set Threshold**: Adjust the similarity threshold with the slider (default is 90%).
3. **Process & Download**: Click the button to remove redundant pages and download the optimized PDF.

## Usage

1. **Clone the repository and navigate into the project**:
   ```bash
   git clone https://github.com/dennismstfc/Incremental-PDF-Page-Remover
   cd Incremental-PDF-Page-Remover
   ```

2. **Create a virtual environment and activate it**:
- For macOS/Linux:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
- For Windows:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app**:
   ```bash
   streamlit run main.py
   ```

5. **Upload PDF**: Drag and drop a file.

6. **Adjust Threshold & Process**: Set the similarity threshold and click to remove redundant pages.

## Author
Made with ❤️ by [Dennis Mustafić](https://github.com/dennismstfc)
