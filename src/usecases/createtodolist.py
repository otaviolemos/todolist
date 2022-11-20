from src.entities.todolist import TodoList
from src.usecases.errors.invalidusererror import InvalidUserError
from src.usecases.errors.duplicatetodolisterror import DuplicateTodoListError

class CreateTodoList:
    def __init__(self, user_repo, todolist_repo):
      self.user_repo = user_repo
      self.todolist_repo = todolist_repo

    def perform(self, user_email):
      owner = self.user_repo.find_by_email(user_email)
      if not owner:
          raise InvalidUserError
      user_already_has_todolist = self.todolist_repo.find_by_email(user_email)
      if user_already_has_todolist:
          raise DuplicateTodoListError
      new_todolist = TodoList(owner)
      self.todolist_repo.add(new_todolist)