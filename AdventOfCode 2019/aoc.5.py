import sys
import os
sys.path.append(os.path.abspath("../"))
sys.path.append(os.path.abspath("../AdventOfCode 2020/"))
from utils import *
from aoc import *
from session import SESSION
from datetime import datetime
import numpy as np

aoc = AOC(session=SESSION)

# aoc.verify_session()

data = list(map(int, aoc.get_file(year=2019, day=5).brut.split(',')))

import time

def intcode(a: list, inp: list) -> list:
    i = 0
    output = []
    while i < len(a):
        # time.sleep(0.5)
        op = a[i] % 100
        try:
            xi = a[i + 1] if (a[i] // 100) % 10 == 0 else i + 1
            x = a[xi]
        except IndexError:
            xi = None
        try:
            yi = a[i + 2] if (a[i] // 1000) % 10 == 0 else i + 2
            y = a[yi]
        except IndexError:
            xi = None
        try:
            zi = a[i + 3] if (a[i] // 10000) % 10 == 0 else i + 3
            z = a[zi]
        except IndexError:
            xi = None

        print(op)

        if op == 1 or op == 0:
            a[zi] = x + y
            i += 4
        elif op == 2:
            a[zi] = x * y
            i += 4
        elif op == 3:
            a[xi] = inp.pop(0)
            i += 2
        elif op == 4:
            output.append(x)
            i += 2
        elif op == 5:
            if x != 0:
                i = y
            else:
                i += 3
        elif op == 6:
            if x == 0:
                i = y
            else:
                i += 3
        elif op == 7:
            a[zi] = int(x < y)
            i += 4
        elif op == 8:
            a[zi] = int(x == y)
            i += 4
        elif op == 99:
            print('End')
            break
        else:
            print('Error')
            break
    print(i)
    return output


print(data)
print(intcode(data, [5]))
