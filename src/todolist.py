from duplicateitemerror import DuplicateItemError

class TodoList:
    def __init__(self, owner):
        self.owner = owner
        self.list = []

    def add(self, item):
        if self.find(item.description) != None:
            raise DuplicateItemError()
        self.list.append(item)
        self.sort()

    def get(self, index):
        return self.list[index]

    def get_owner(self):
        return self.owner

    def complete_item(self, index):
        self.list[index].complete()

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

    def change_priority(self, index, new_priority):
        self.list[index].change_priority(new_priority)
        self.list.sort()