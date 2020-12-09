import itertools


class Set:
    @staticmethod
    def permutations(*args, **kwargs) -> list:
        """ Calculate all permutations of list.

        Returns:
            All permutations
        """
        return list(itertools.permutations(*args, **kwargs))
