from abc import ABC, abstractmethod


class Expression(ABC):
    @abstractmethod
    def reduce(self, to):
        raise NotImplementedError
