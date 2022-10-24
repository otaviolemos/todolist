class TodoList:
    def __init__(self, owner):
        self.owner = owner
        self.list = []

    def add(self, item):
        self.list.append(item)

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