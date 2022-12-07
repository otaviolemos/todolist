class RemoveItem():
    def __init__(self, todolist_repo):
        self.todolist_repo = todolist_repo

    def perform(self, user_email, item_description):
        todolist = self.todolist_repo.find_by_email(user_email)
        todolist.remove_by_description(item_description)
        self.todolist_repo.update(user_email, todolist)