
from Errors import ERROR_CLASS_MAPPING


class RichException(Exception):
    def __init__(self, code):
        super().__init__()
        self.error = ERROR_CLASS_MAPPING[code]()

