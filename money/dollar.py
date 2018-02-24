class Dollar:
    def __init__(self, amount):
        self.__amount = amount

    def times(self, multiplier):
        return Dollar(self.__amount * multiplier)

    def __eq__(self, other):
        return self.__amount == other.__amount
