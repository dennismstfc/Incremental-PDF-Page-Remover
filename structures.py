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

    def remove_incremental_pages(self):
        """
        Goal of this function is to remove incremental pages from the script, which lead to redundancy.
        We define incremental pages as those whose content is at least 80% similar to the previous page.
        """
        if not self.pages:
            raise ValueError("No pages found in the script.")
        
        filtered_pages = []
        i = 0

        while i < len(self.pages):
            current_page = self.pages[i]
            # Check subsequent pages for incremental content
            while i + 1 < len(self.pages) and self.is_incremental(current_page, self.pages[i + 1]):
                i += 1
                current_page = self.pages[i]
            
            filtered_pages.append(current_page)
            i += 1
        
        self.pages = filtered_pages
        self.page_numbers = [page.page_no for page in filtered_pages]

    def is_incremental(self, page1: Page, page2: Page, threshold: float = 0.9) -> bool:
        """
        Check if two pages are incremental based on content similarity.
        A simple way to calculate similarity is to compare the length of the intersection
        of their words to the union of their words.
        :return: True if the pages are incremental, False otherwise.
        """
        content1 = set(" ".join(page1.content).split())
        content2 = set(" ".join(page2.content).split())
        
        if not content1 or not content2:
            return False  # If one of the pages has no content, they're not similar

        intersection = content1.intersection(content2)
        union = content1.union(content2)

        similarity = len(intersection) / len(union)
        return similarity >= threshold
