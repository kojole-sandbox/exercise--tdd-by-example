from .expression import Expression


class Money(Expression):
    def __init__(self, amount, currency):
        self._amount = amount
        self._currency = currency

    def __eq__(self, other):
        return self._amount == other._amount and self.currency() == other.currency()

    def __repr__(self):
        return '<{} {}>'.format(self._amount, self._currency)

    def currency(self):
        return self._currency

    def plus(self, other):
        return Money(self._amount + other._amount, self.currency())

    def times(self, multiplier):
        return Money(self._amount * multiplier, self._currency)

    @staticmethod
    def dollar(amount):
        return Money(amount, 'USD')

    @staticmethod
    def franc(amount):
        return Money(amount, 'CHF')
