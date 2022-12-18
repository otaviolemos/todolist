class RemoveTodoList:
    def __init__(self, todo_list_repository):
        self.todo_list_repository = todo_list_repository

    def perform(self, user_email):
        self.todo_list_repository.remove(user_email)
        