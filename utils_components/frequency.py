import collections


class Frequency:
    @staticmethod
    def count_occurrences(lst: list) -> dict:
        """ Amount of occurrences of each items in list

        Args:
            lst: List where to count

        Returns:
            Dictionary of occurrences
        """
        occurrences = collections.defaultdict(lambda: 0)
        for val in lst:
            occurrences[val] += 1
        return occurrences
