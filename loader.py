from pathlib import Path
from PyPDF2 import PdfReader
import os

from standard_values import BASE_DIR
from structures import page, script

class PDFLoader:
    def __init__(self, path: Path):
        # Make sure scripts/ folder exists, if not create it
        if not BASE_DIR.exists():
            os.mkdir(BASE_DIR)

        if not path.exists():
            raise FileNotFoundError(f"File not found: {path}")

        self.path = path
        self.load_pdf()
    
    def load_pdf(self):
        reader = PdfReader(self.path)
        pages = reader.pages
        self.no_pages = len(pages)
        page_objects = []

        for idx, act_page in enumerate(pages):
            content = act_page.extract_text()

            tmp_page = page(idx, content)
            page_objects.append(tmp_page)

        self.script = script(self.path.stem, page_objects)
    
    def get_script(self):
        return self.script  
