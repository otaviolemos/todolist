from src.usecases.errors.invalidusererror import InvalidUserError


class GetTodoList():
    def __init__(self, todolist_repository):
        self.todolist_repository = todolist_repository

    def perform(self, user_email):
        todolist = self.todolist_repository.find_by_email(user_email)
        if not todolist:
            raise InvalidUserError()
        return todolist