from src.entities.todoitem import TodoItem

class CreateTodoItem:
    def __init__(self, user_repo, todolist_repo):
      self.user_repo = user_repo
      self.todolist_repo = todolist_repo

    def perform(self, user_email, item_description, item_priority):
      todolist = self.todolist_repo.find_by_email(user_email)
      todoitem = TodoItem(item_description, item_priority)
      todolist.add(todoitem)
      self.todolist_repo.update(user_email, todolist)