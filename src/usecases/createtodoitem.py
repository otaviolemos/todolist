from src.entities.todoitem import TodoItem
from src.usecases.errors.invalidusererror import InvalidUserError

class CreateTodoItem:
    def __init__(self, todolist_repo):
      self.todolist_repo = todolist_repo

    def perform(self, user_email, item_description, item_priority):
      todolist = self.todolist_repo.find_by_email(user_email)
      if not todolist:
        raise InvalidUserError()
      todoitem = TodoItem(item_description, item_priority)
      todolist.add(todoitem)
      self.todolist_repo.update(user_email, todolist)