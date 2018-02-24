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

    def plus(self, addend):
        from .sum import Sum
        return Sum(self, addend)

    def reduce(self, bank, to):
        rate = bank.rate(self._currency, to)
        return Money(self._amount / rate, to)

    def times(self, multiplier):
        return Money(self._amount * multiplier, self._currency)

    @staticmethod
    def dollar(amount):
        return Money(amount, 'USD')

    @staticmethod
    def franc(amount):
        return Money(amount, 'CHF')
