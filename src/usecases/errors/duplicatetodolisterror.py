class DuplicateTodoListError(Exception):
        def __init__(self):
            message = 'User already has todo list.'
            super().__init__(message)