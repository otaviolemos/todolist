class TodoItem:
    def __init__(self, description):
        self.description = description
        self.done = False

    def complete(self):
        self.done = True

    def is_done(self):
        return self.done

    def undo(self):
        self.done = False

    def change_description(self, description):
        self.description = description