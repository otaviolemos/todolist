class TodoItem:
    def __init__(self, description, priority):
        self.description = description
        self.completed = False
        self.priority = priority

    def __lt__(self, other):
        return self.priority.value < other.priority.value

    def complete(self):
        self.completed = True

    def is_completed(self):
        return self.completed

    def undo(self):
        self.completed = False

    def change_description(self, new_description):
        self.description = new_description

    def change_priority(self, new_priority):
        self.priority = new_priority
