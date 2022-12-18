from src.usecases.errors.invaliduserotnotodolist import InvalidUserOrNoTodoList


class RemoveTodoList:
    def __init__(self, todo_list_repository):
        self.todo_list_repository = todo_list_repository

    def perform(self, user_email):
        if not self.todo_list_repository.find_by_email(user_email):
            raise InvalidUserOrNoTodoList()
        self.todo_list_repository.remove(user_email)
