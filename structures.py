from typing import List

class Page:
    def __init__(self, page_no: int, content: List[str]):
        self.page_no = page_no
        self.content = content

class Script:
    def __init__(self, title: str, pages: List[Page]):
        self.title = title
        self.pages = pages
        self.page_numbers = [page.page_no for page in pages]