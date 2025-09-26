import logging
from rich.logging import RichHandler


class Logger(logging.Logger):
    _instances = {}

    def __new__(cls, name, level=logging.INFO, log_file=None):
        """Direct implementation of singleton pattern."""
        if name in cls._instances:
            return cls._instances[name]

        instance = super().__new__(cls)
        cls._instances[name] = instance
        return instance

    def __init__(self, name, level=logging.INFO, log_file=None):
        """Force to rebuild attributes of logger created to avoid side effects of another libs."""
        super().__init__(name, level)

        if not self.hasHandlers():
            console_handler = RichHandler(rich_tracebacks=True)
            console_handler.setLevel(level)
            self.addHandler(console_handler)

            if log_file:
                file_handler = logging.FileHandler(log_file)
                file_handler.setLevel(level)
                file_handler.setFormatter(
                    logging.Formatter(
                        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
                    )
                )
                self.addHandler(file_handler)
