import fractions
import random
from typing import Callable


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
