from abc import ABC, abstractmethod


class HashService(ABC):
    @abstractmethod
    def hash(self, password):
        raise (NotImplementedError)

    @abstractmethod
    def check(self, password, hashed):
        raise (NotImplementedError)
