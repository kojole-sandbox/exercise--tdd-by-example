from .expression import Expression
from .money import Money


class Sum(Expression):
    def __init__(self, augend, addend):
        self.augend = augend
        self.addend = addend

    def reduce(self, bank, to):
        amount = self.augend._amount + self.addend._amount
        return Money(amount, to)
