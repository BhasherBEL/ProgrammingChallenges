import itertools
import collections
from abc import ABC

import sortedcontainers


class Set:
    @staticmethod
    def permutations(*args, **kwargs) -> list:
        """ Calculate all permutations of list.

        Returns:
            All permutations
        """
        return list(itertools.permutations(*args, **kwargs))

    class SortedDict(sortedcontainers.SortedDict):
        pass

    class SortedSet(sortedcontainers.SortedSet):
        pass

    class SortedList(sortedcontainers.SortedList, ABC):
        pass

    class DefaultDict(collections.defaultdict):
        pass

    class DefaultSortedDict(collections.defaultdict, sortedcontainers.SortedDict):
        def __init__(self, default_factory=None, *args, **kwargs):
            super().__init__(default_factory=default_factory, *args, **kwargs)
            #sortedcontainers.SortedDict.__init__(self, *args, **kwargs)
            #collections.defaultdict.__init__(self, default_factory)
