from src.usecases.errors.invalidusererror import InvalidUserError


class ChangeItemDescription():
    def __init__(self, todolist_repo):
        self.todolist_repo = todolist_repo

    def perform(self, user_email, old_description, new_description):
        todolist = self.todolist_repo.find_by_email(user_email)
        if not todolist:
            raise InvalidUserError()
        todolist.change_description(old_description, new_description)
        self.todolist_repo.update(user_email, todolist)