from collections.abc import Iterable


class Iter:
    @staticmethod
    def sequences(data: list, size: int, step: int = None) -> list:
        if step is None:
            step = size
        for i in range(0, len(data) - size + 1, step):
            yield data[i:i + size]

    @staticmethod
    def deep_enumerate(it: Iterable, depth: int = None):
        if isinstance(it, dict):
            it = list(it.values())

        if depth is None and not isinstance(it[0], Iterable):
            depth = 1

        for i, v in enumerate(it):
            if depth == 1:
                yield i, v
            else:
                for u in Iter.deep_enumerate(v, depth=None if depth is None else depth - 1):
                    yield i, *u

    @staticmethod
    def deep_index(dic: dict):
        if not isinstance(dic, dict):
            yield dic,
            return

        for k, v in dic.items():
            for u in Iter.deep_index(v):
                yield k, *u

    @staticmethod
    def multimove(data: list, size: int) -> list:
        for i in range(len(data) - size + 1):
            yield data[i:i + size]
