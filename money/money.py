from abc import ABC, abstractmethod


class Money(ABC):
    def __init__(self, amount, currency):
        self._amount = amount
        self._currency = currency

    def __eq__(self, other):
        return self._amount == other._amount and self.__class__ == other.__class__

    def currency(self):
        return self._currency

    @abstractmethod
    def times(self):
        pass

    @staticmethod
    def dollar(amount):
        from .dollar import Dollar
        return Dollar(amount, 'USD')

    @staticmethod
    def franc(amount):
        from .franc import Franc
        return Franc(amount, 'CHF')
