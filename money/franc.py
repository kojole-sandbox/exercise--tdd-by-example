from .money import Money


class Franc(Money):
    def times(self, multiplier):
        return Money.franc(self._amount * multiplier)
