class TodoItem:
    def __init__(self, description, priority):
        self.description = description
        self.completed = False
        self.priority = priority

    def __lt__(self, other):
        if (not self.completed) and (not other.completed):
            return self.priority.value < other.priority.value
        if self.completed and (not other.completed):
            return False
        if (not self.completed) and other.completed:
            return True
        return False
        

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
