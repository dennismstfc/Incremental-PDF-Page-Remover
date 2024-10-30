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
            return

        # Start with the first page
        filtered_pages = [self.pages[0]]

        for current_page in self.pages[1:]:
            previous_page = filtered_pages[-1]
            if not self.is_incremental(previous_page, current_page):
                filtered_pages.append(current_page)
            else:
                print(f"Removing incremental page {current_page.page_no}")

        self.pages = filtered_pages
        self.page_numbers = [page.page_no for page in filtered_pages]

    def is_incremental(self, page1: Page, page2: Page, threshold: float = 0.8) -> bool:
        """
        Check if two pages are incremental based on content similarity.
        A simple way to calculate similarity is to compare the length of the intersection
        of their words to the union of their words.
        """
        content1 = set(" ".join(page1.content).split())
        content2 = set(" ".join(page2.content).split())
        
        if not content1 or not content2:
            return False  # If one of the pages has no content, they're not similar

        intersection = content1.intersection(content2)
        union = content1.union(content2)

        similarity = len(intersection) / len(union)
        return similarity >= threshold

    def print_example_content(self, amount_chars: int = 150):
        for page in self.pages:
            print(f"Page {page.page_no}:")
            # Print first 50 characters of the page content, if possible. Make sure there are enough characters
            # to print
            if len(page.content) > amount_chars:
                print("".join(page.content[:amount_chars]))
            else:
                print("".join(page.content))

            print("\n")
    
    def print_final_script(self):
        for page in self.pages:
            print(f"Page {page.page_no}:")
            print("".join(page.content))
            print("\n")