from utils import experiment


def num_coins(
    cents: int,
    coins: list[int] = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000]
):
    """Convert an amount of cents to minimal amount of coins
    
    Arguments:
        cents: Amount of cents
        coins: list of possible coins

    Returns:
        dict: Dictinnary of optimized coins
    """
    coins.sort(reverse=True)
    
    resultats = {}
    for coin in coins:
        amount = cents//coin
        if amount > 0:
            resultats[coin] = amount
            cents -= amount*coin
    
    return resultats

def fibonacci(n):
    f = [0]*n
    f[1] = 1
    for i in range(2, n):
        f[i] = f[i-1] + f[i-2]
    return f[-1]

# experiment(fibonacci, {n: 200}, duration=5)

def factorial_rec(n):
    if n < 2:
        return 1
    
    return factorial_rec(n-1) * n

def factorial_it(n):
    res = 1
    for i in range(2, n+1):
        res *= i
    return res

# experiment(factorial_rec, {'n': 1000}, duration=2)
# experiment(factorial_it, {'n': 1000}, duration=2)

def climbing_staircase_rec(n, mem=None):
    if mem is None:
        mem = {}
    
    if n == 1:
        return 1
    if n == 2:
        return 2
    mem[n] = climbing_staircase_rec(n-1, mem) + climbing_staircase_rec(n-2, mem)
    return mem[n]

def climbing_staircase_it(n):    
    f = [0]*(n+1)
    f[1] = 1
    f[0] = 1
    for i in range(2, n+1):
        f[i] = f[i-1] + f[i-2]
    return f[-1]


# experiment(climbing_staircase_rec, n=20, duration=2)
# experiment(climbing_staircase_it, n=20, duration=2)


def sort(lst):
    out = []
    for c in lst:
        if len(out) == 0:
            out.append(c)
        else:
            for i, el in enumerate(out):
                if c >= el:
                    out.insert(i, c)
                    break
    return out

# import random

# a = list(range(1000))
# random.shuffle(a)
# b = a.copy()
# c = a.copy()
# d = a.copy()

# experiment(sort, lst=a, duration=2)
# experiment(lambda x: x.copy().sort(), x=c, duration=2)
# experiment(lambda x: sorted(x), x=d, duration=2)

# https://www.techiedelight.com/longest-common-subsequence/
def base(a: str, b: str, i: int, j: int):
    res = []
    for k in range(0, min(i, j)+1):
        if a[i-k] == b[j-k]:
            res.append(a[i-k])
        else:
            break
    return ''.join(reversed(res))
    
def longestCommonSubsequence(a: str, b: str) -> str:
    biggest = ''
    for i, c in enumerate(a):
        for j, d in enumerate(b):
            if c == d:
                current = base(a, b, i, j)
                if len(current) > len(biggest):
                    biggest = current
    
    return biggest

experiment(longestCommonSubsequence, a='ABCBDABABIFGHFOGDFHGDFIGFHGOFGHRGHDROGDGHDROGR', b='BDCABFNOGFHGOFXWDPFOHFDSFDDFLDDSOA', duration=2)