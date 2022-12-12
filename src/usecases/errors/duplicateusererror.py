class DuplicateUserError(Exception):
        def __init__(self):
            message = 'Duplicate user.'
            super().__init__(message)