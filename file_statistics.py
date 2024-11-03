import csv
from pathlib import Path
from datetime import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from pdf_processor import PDFProcessor
from standard_values import STATISTICS_DIR

class PDFFile:
    def __init__(self, file_path: Path):
        if not file_path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")

        self._full_path = file_path
        self._content = None

    @property
    def file_name(self) -> str:
        return self._full_path.name
    
    @property
    def full_path(self) -> str:
        return str(self._full_path)
    
    @property
    def content(self) -> str:
        if self._content is None:
            try:
                pdf_processor = PDFProcessor(self._full_path)
                self._content = pdf_processor.get_script().get_content()
            except Exception as e:
                raise RuntimeError(f"Error loading the content: {e}")
        return self._content

    @property
    def file_size(self) -> int:
        return self._full_path.stat().st_size        

    @property
    def date_added(self) -> str:
        return self.get_current_date()

    @property
    def time_added(self) -> str:
        return self.get_current_time()

    @staticmethod
    def get_current_time() -> str:
        return datetime.now().strftime('%H:%M:%S')

    @staticmethod
    def get_current_date() -> str:
        return datetime.now().strftime('%d-%m-%Y')


class FileTracker(FileSystemEventHandler):
    def __init__(self, directory: Path, csv_file: Path):
        if not STATISTICS_DIR.exists():
            STATISTICS_DIR.mkdir()

        self.directory = directory
        self.csv_file = Path(STATISTICS_DIR, csv_file)

        if not self.csv_file.exists():
            with open(self.csv_file, mode='w', newline='') as csv_file_handle:
                writer = csv.writer(csv_file_handle)
                writer.writerow([
                    'File Name', 
                    'Full Path',
                    'File Size', 
                    'Date Added', 
                    'Time Added',
#                    'Content'
                    ])

        # Set up the observer
        self.observer = Observer()
        self.observer.schedule(self, self.directory, recursive=False)
        self.observer.start()

    def on_created(self, event):
        """
        Event handler for when a new file is created in the directory.
        """
        if not event.is_directory:
            self.log_new_file(event.src_path)

    def log_new_file(self, file_path: str):
        """
        Log the details of the new file to a CSV file. 
        """
        file = PDFFile(Path(file_path))

        with open(self.csv_file, mode='a', newline='', encoding="utf-8") as csv_file_handle:
            writer = csv.writer(csv_file_handle)
            writer.writerow([
                file.file_name, 
                file.full_path,
                file.file_size, 
                file.date_added, 
                file.time_added,
#                file.content <- this needs to get fixed. The string is currenly not correctly formatted.
                ])

    def stop(self):
        self.observer.stop()
        self.observer.join()


if __name__ == "__main__":
    directory_to_watch = Path("scripts")
    csv_log_file = Path("test.csv")

    tracker = FileTracker(directory_to_watch, csv_log_file)

    try:
        while True:
            pass  # Keep the script running
    except KeyboardInterrupt:
        tracker.stop()
