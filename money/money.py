class Money:
    def __init__(self, amount):
        self._amount = amount

    def __eq__(self, other):
        return self._amount == other._amount
