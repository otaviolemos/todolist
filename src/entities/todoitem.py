class TodoItem:
    def __init__(self, description, priority):
        self.description = description
        self.done = False
        self.priority = priority

    def __lt__(self, other):
        return self.priority.value < other.priority.value

    def complete(self):
        self.done = True

    def is_done(self):
        return self.done

    def undo(self):
        self.done = False

    def change_description(self, new_description):
        self.description = new_description

    def change_priority(self, new_priority):
        self.priority = new_priority