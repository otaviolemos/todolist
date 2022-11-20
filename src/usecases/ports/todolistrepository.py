from abc import ABC, abstractmethod


class TodoListRepository(ABC):
    @abstractmethod
    def add(self, todolist):
        raise (NotImplementedError)

    @abstractmethod
    def find_by_email(self, user_email):
        raise (NotImplementedError)

    @abstractmethod
    def update(self, user_email, newtodolist):
        raise (NotImplementedError)
