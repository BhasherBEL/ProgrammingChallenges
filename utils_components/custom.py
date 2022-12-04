import collections


class Custom:
    @staticmethod
    def defaultdict(fct, depth=1):
        if depth <= 1:
            return collections.defaultdict(fct)
        else:
            return collections.defaultdict(lambda: Custom.defaultdict(fct, depth=depth-1))