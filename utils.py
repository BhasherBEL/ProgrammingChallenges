import random
import collections
import re
from typing import Union, Optional, Callable
import fractions
import itertools


class Summon:
    @staticmethod
    def how_sum(target: int, lst: list[int], memory: Optional[dict] = None) -> Optional[list[int]]:
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
    def sum2(target: int, lst: list[int], first_only: bool = True, multiple: bool = True, reverted: bool = False) -> Union[
        tuple[int, int], None, set[tuple[int, int]]]:
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


class Parse:
    @staticmethod
    def one_line_dict(line: str) -> dict:
        """ Parse a one-line dict into real dict object.

        Args:
            line: String to parse

        Returns:
            Dictionary of parsed values
        """
        return {k.strip(): v.strip() for k, v in re.findall(r'^([^,]*?): ?(.+?) ?$', line.strip().replace(',', '\n'), flags=re.MULTILINE)}


class Number:
    @staticmethod
    def is_prime(n: int) -> bool:
        """Primality test using 6k+-1 optimization.
        Args:
            n: Number to check primality

        Returns:
            If n is prime
        """
        if n <= 3:
            return n > 1
        if not n % 2 or not n % 3:
            return False
        i = 5
        while i ** 2 <= n:
            if not n % i or not n % (i + 2):
                return False
            i += 6
        return True

    @staticmethod
    def is_probably_prime(n: int, k: int = 10) -> bool:
        """Primality test using probability optimization.
        Args:
            n: Number to check primality
            k: Amount of check to do

        Returns:
            If n is probably prime
        """
        if n == 1 or n == 4:
            return False
        elif n == 2 or n == 3:
            return True
        else:
            for i in range(k):
                a = random.randint(2, n - 2) % n
                res = 1
                o = n-1

                while o > 0:
                    if o % 2:
                        res = (res * a) % n
                        o -= 1
                    else:
                        a = (a ** 2) % n
                        o //= 2

                if res % n != 1:
                    return False

        return True

    @staticmethod
    def primes_before(n: int, method: Callable = is_prime) -> list[int]:
        """ Find all prime numbers between 0 and n.

        Args:
            n: Maximum value
            method: Primality test method

        Returns:

        """
        candidates = list(range(3, n+1, 2))
        primes = []

        while candidates:
            candidate = candidates.pop(0)
            if method.__func__(candidate):
                primes.append(candidate)
                if candidate*2 <= n:
                    candidates = [x for x in candidates if x % candidate]

        if n > 1:
            primes.insert(0, 2)

        return primes

    @staticmethod
    def gcd(*args, **kwargs) -> int:
        """ Calculate gcd of two numbers

        Returns:
            gcd of given numbers
        """
        return fractions.gcd(*args, **kwargs)

    @staticmethod
    def factorial(n: int, memory: dict = {}) -> int:
        """ Calculate the factorial of number

        Args:
            n: Number to calculate
            memory: Dynamic programming memory

        Returns:

        """
        if n in memory:
            return memory[n]

        if n == 1:
            return 1
        else:
            memory[n] = Number.factorial(n-1) * n
            return memory[n]


class Set:
    @staticmethod
    def permutations(*args, **kwargs) -> list:
        """ Calculate all permutations of list.

        Returns:
            All permutations
        """
        return list(itertools.permutations(*args, **kwargs))
