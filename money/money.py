class Money:
    def __init__(self, amount, currency):
        self._amount = amount
        self._currency = currency

    def __eq__(self, other):
        return self._amount == other._amount and self.currency() == other.currency()

    def currency(self):
        return self._currency

    def times(self, multiplier):
        return Money(self._amount * multiplier, self._currency)

    @staticmethod
    def dollar(amount):
        from .dollar import Dollar
        return Dollar(amount, 'USD')

    @staticmethod
    def franc(amount):
        from .franc import Franc
        return Franc(amount, 'CHF')
