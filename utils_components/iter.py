class Iter:
    @staticmethod
    def sequences(data: list, size: int) -> list:
        for i in range(0, len(data), size):
            yield data[i:i+size]

    @staticmethod
    def custom_sequences(data: list, size: int) -> list:
        for i in range(0, len(data), size):
            yield [Iter.SequencedPart(data, i+j) for j in range(size)]

    class SequencedPart(object):
        def __init__(self, data_source: list, position: int) -> None:
            self.data_source = data_source
            self.position = position
            print(self.__class__.__setattr__(self, '__mro__', (self.__class__, data_source[position].__class__, object)))
            # self.__setattr__('__mro__')

        def set(self, value: any) -> None:
            self.data_source[self.position] = value
