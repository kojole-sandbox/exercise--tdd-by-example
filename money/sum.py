from .expression import Expression
from .money import Money


class Sum(Expression):
    def __init__(self, augend, addend):
        self.augend = augend
        self.addend = addend

    def plus(self, addend):
        pass

    def reduce(self, bank, to):
        amount = (self.augend.reduce(bank, to)._amount +
                  self.addend.reduce(bank, to)._amount)
        return Money(amount, to)
