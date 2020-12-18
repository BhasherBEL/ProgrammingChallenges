from collections.abc import Iterable


class Iter:
    @staticmethod
    def sequences(data: list, size: int) -> list:
        for i in range(0, len(data), size):
            yield data[i:i+size]

    @staticmethod
    def deeply(it: Iterable, depth=None):
        if isinstance(it, dict):
            it = list(it.values())
        else:
            it = list(it)

        if depth is None and not isinstance(it[0], Iterable):
            depth = 1

        if depth == 1:
            for i, v in enumerate(it):
                yield (i, v)
        else:
            for i, sit in enumerate(it):
                for u in Iter.deeply(sit, depth=None if depth is None else depth-1): # ceci est un test
                    yield (i, *u)

    @staticmethod
    def multirange(*args, depth=1, **kwargs):
        pass
