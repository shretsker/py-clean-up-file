import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self: object) -> object:
        return self

    def __exit__(
            self,
            exc_type: str,
            exc_value: str,
            traceback: str
    ) -> bool:
        if os.path.exists(self.filename):
            os.remove(self.filename)
        return False
