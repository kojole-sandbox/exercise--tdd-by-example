from abc import ABC, abstractmethod


class Money(ABC):
    def __init__(self, amount):
        self._amount = amount

    def __eq__(self, other):
        return self._amount == other._amount and self.__class__ == other.__class__

    @abstractmethod
    def times(self):
        pass

    @staticmethod
    def dollar(amount):
        from .dollar import Dollar
        return Dollar(amount)

    @staticmethod
    def franc(amount):
        from .franc import Franc
        return Franc(amount)
