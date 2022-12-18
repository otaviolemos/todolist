class InvalidUserOrNoTodoList(Exception):
      def __init__(self):
          message = 'Invalid user or user with no todo list.'
          super().__init__(message)