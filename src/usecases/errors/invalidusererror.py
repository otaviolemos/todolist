class InvalidUserError(Exception):
        def __init__(self):
            message = 'Invalid user.'
            super().__init__(message)