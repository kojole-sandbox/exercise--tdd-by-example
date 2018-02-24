class Bank:
    def __init__(self):
        self.__rates = dict()

    def add_rate(self, from_, to, rate):
        self.__rates[(from_, to)] = rate

    def rate(self, from_, to):
        if from_ == to:
            return 1
        return self.__rates[(from_, to)]

    def reduce(self, source, to):
        return source.reduce(self, to)
