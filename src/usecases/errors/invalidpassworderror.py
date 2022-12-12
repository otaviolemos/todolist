class InvalidPasswordError(Exception):
        def __init__(self):
            message = 'Invalid password.'
            super().__init__(message)