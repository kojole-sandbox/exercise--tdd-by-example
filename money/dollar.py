from .money import Money


class Dollar(Money):
    def times(self, multiplier):
        return Money.dollar(self._amount * multiplier)
