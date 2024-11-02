from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter
import os

from standard_values import BASE_DIR, PROCESSED_SCRIPTS_DIR
from structures import Page, Script

class PDFProcessor:
    def __init__(self, path: Path, should_remove: bool = True):
        # Making sure scripts/ folder exists, if not create it
        if not BASE_DIR.exists():
            os.mkdir(BASE_DIR)
        
        # Making sure processed_scripts/ folder exists, if not create it
        if not PROCESSED_SCRIPTS_DIR.exists():
            os.mkdir(PROCESSED_SCRIPTS_DIR)

        if not path.exists():
            raise FileNotFoundError(f"File not found: {path}")

        self.path = path
        self.should_remove = should_remove
        self._load_pdf()
    
    def _load_pdf(self):
        """
        Load the PDF file and extract its content.
        """
        self.reader = PdfReader(self.path)
        pages = self.reader.pages
        self.no_pages = len(pages)
        page_objects = []

        for idx, act_page in enumerate(pages):
            content = act_page.extract_text()

            tmp_page = Page(idx, content)
            page_objects.append(tmp_page)

        self.script = Script(self.path.stem, page_objects)

        if self.should_remove:
            self.script.remove_incremental_pages()

    def create_pdf_without_redundancy(self):
        """
        Goal of this function is to create a new PDF file without the redundant pages.
        :return: Path to the new PDF file.
        """
        writer = PdfWriter()
        pages_to_keep = self.script.page_numbers

        for idx in pages_to_keep:
            writer.add_page(self.reader.pages[idx])

        output_path = PROCESSED_SCRIPTS_DIR / f"{self.path.stem}_processed.pdf"
        with open(output_path, "wb") as f:
            writer.write(f)
        
        return output_path

    def get_script(self):
        """
        :return: Script object representing the PDF content.
        """
        return self.script  
