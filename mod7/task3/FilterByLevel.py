import logging


class FilterByLevel(logging.Handler):
    def __init__(self, mode='w'):
        super().__init__()
        self.mode = mode
        self.formatter = logging.Formatter(fmt="%(levelname)s | %(name)s | %(asctime)s | %(lineno)d | %(message)s")

    def emit(self, record: logging.LogRecord) -> None:
        message = self.format(record)
        with open(f'logs_by_level/calc_{record.levelname.lower()}.log', mode=self.mode) as f:
            f.write(message + '\n')
