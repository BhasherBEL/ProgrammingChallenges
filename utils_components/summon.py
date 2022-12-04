import itertools
from typing import Union, Optional


class Summon:
    @staticmethod
    def how_sum(target: int, lst: list, memory: Optional[dict] = None) -> Optional[list]:
        """ finds a combination of elements that, when summoned, is equal to the target.

        Create and optimized by Alexandre Dewilde.

        Args:
            target: Number to reach
            lst: List of usable numbers
            memory: Dynamic programming memory

        Returns:
            The combination of elements
        """
        if memory is None:
            memory = {}

        if target in memory:
            return memory[target]
        if target == 0:
            return []
        if target < 0:
            return None

        for el in lst:
            res = Summon.how_sum(target - el, lst, memory)
            if res is not None:
                memory[target] = res + [el]
                return memory[target]
        memory[target] = None

    @staticmethod
    def sum2(target: int, lst: list, first_only: bool = True, multiple: bool = True, reverted: bool = False) -> Union[tuple, None, set]:
        """ Finds the pair(s) of additive elements that give the target.

        Based on Alexandre Dewilde version.

        Args:
            target: Number to reach
            lst: List of usable numbers
            first_only: Boolean if only the first solution needs to be returned
            multiple: Boolean if the target can be twice the same number
            reverted: Boolean if both directions must be returned

        Returns:
            The solution(s) found
        """
        possibilities = set()
        for el in frozenset(lst):
            remainder = target - el
            if (multiple or el != remainder) and remainder in lst:
                if first_only:
                    return el, remainder
                possibilities.add((el, remainder) if reverted else frozenset({el, remainder}))
        if first_only:
            return None
        return possibilities

    @staticmethod
    def sum_to_n(n: int) -> int:
        """ Calculate sum of all numbers between 0 and n

        Args:
            n: Maximum value to add

        Returns:
            Sum of all numbers
        """
        return list(itertools.accumulate(range(1, n+1)))[-1]
