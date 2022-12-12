class DuplicateItemError(Exception):
        def __init__(self):
            message = 'Duplicate item.'
            super().__init__(message)