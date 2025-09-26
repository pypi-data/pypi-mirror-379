"""Loading related classes

    This module consists of classes that help display progress/loading
    to make user wait patiently and indicate a process is happening.
"""
import time
import threading
from rich.progress import (
    Progress,
    SpinnerColumn,
    TextColumn,
    BarColumn,
    DownloadColumn,
    TransferSpeedColumn,
    TimeRemainingColumn,
)


class Spinner:
    """
    Displays a spinner in terminal to indicate user a process is happening
    """

    def __init__(self) -> None:
        self.loading_thread = None
        self.loading_stop_event = None
        self.is_stopped = True

    def _show_loading_spinner(self, stop_event: threading.Event, msg: str):
        """
        This function displays the loading circle and message

        :stop_event: a threading event to stop the spinner
        :msg: message to be displayed while loading.
        """
        with Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                transient=True,
        ) as progress:
            progress.add_task(description=f"{msg}...", total=None)
            while True:
                if stop_event.is_set():
                    break
                time.sleep(0.1)

    def start(self, msg: str) -> None:
        """
        This function starts the spinner and displays the loading/progress message.

        :msg: message to be displayed while loading.
        """
        self.is_stopped = False
        self.loading_stop_event = threading.Event()
        self.loading_thread = threading.Thread(
            target=self._show_loading_spinner,
            args=(self.loading_stop_event, msg)
        )
        self.loading_thread.start()

    def stop(self):
        """Stop the spinner and clear the progress display."""
        if self.loading_stop_event is not None:
            self.loading_stop_event.set()
        if self.loading_thread is not None:
            self.loading_thread.join()
        self.is_stopped = True


class ProgressBar:
    """
    Displays a progress bar in terminal to indicate file upload progress.
    """
    def __init__(self, total_bytes: int, description: str = "Uploading"):
        self.total_bytes = total_bytes
        self.description = description
        self.progress = Progress(
            # SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            DownloadColumn(),
            TransferSpeedColumn(),
            TimeRemainingColumn(),
            transient=True,
        )
        self.task_id = None

    def __enter__(self):
        self.progress.__enter__()
        self.task_id = self.progress.add_task(self.description, total=self.total_bytes)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.progress.__exit__(exc_type, exc_val, exc_tb)

    def advance(self, bytes_uploaded: int):
        """Advance the progress bar by a number of bytes."""
        self.progress.update(self.task_id, advance=bytes_uploaded)

    def complete(self):
        """Mark the progress bar as complete."""
        self.progress.update(self.task_id, completed=self.total_bytes)
