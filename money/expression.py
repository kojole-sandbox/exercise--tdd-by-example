from abc import ABC, abstractmethod


class Expression(ABC):
    @abstractmethod
    def plus(self, addend):
        raise NotImplementedError

    @abstractmethod
    def reduce(self, bank, to):
        raise NotImplementedError

    @abstractmethod
    def times(self, multiplier):
        raise NotImplementedError
