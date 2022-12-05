from src.entities.errors.duplicateitemerror import DuplicateItemError


class TodoList:
    def __init__(self, owner):
        self.owner = owner
        self.list = []

    def add(self, item):
        self.check_duplicate(item.description)
        self.list.append(item)
        self.sort()

    def get(self, index):
        return self.list[index]

    def get_owner(self):
        return self.owner

    def complete(self, index):
        self.list[index].complete()
        self.sort()

    def complete_by_description(self, description):
        item = self.find(description)
        if item:
            item.complete()
            self.sort()

    def remove(self, index):
        self.list.pop(index)

    def size(self):
        return len(self.list)

    def find(self, description):
        for item in self.list:
            if item.description == description:
                return item

    def sort(self):
        self.list.sort()

    def change_priority_by_index(self, index, new_priority):
        self.list[index].change_priority(new_priority)
        self.list.sort()

    def change_priority_by_description(self, description, new_priority):
        item = self.find(description)
        if not item:
            return
        item.change_priority(new_priority)
        self.list.sort()

    def change_description(self, old_description, new_description):
        self.check_duplicate(new_description)
        item = self.find(old_description)
        if item:
            item.change_description(new_description)

    def check_duplicate(self, description):
        duplicate_item = self.find(description)
        if duplicate_item:
            raise DuplicateItemError()