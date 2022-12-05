class ChangeItemPriority:
    def __init__(self, todo_list_repository):
        self.todo_list_repository = todo_list_repository

    def perform(self, user_email, item_description, new_priority):
        todo_list = self.todo_list_repository.find_by_email(user_email)
        todo_list.change_priority_by_description(item_description, new_priority)
        self.todo_list_repository.update(user_email, todo_list)