import math

class KDTree(object):
    # O(n log² n)
    def __setup(self, data, i=1, dim=0):
        if not len(data):
            return
        
        data = sorted(data, key=lambda x: x[dim])
        self.array[i] = data[len(data)//2]
        self.__setup(data[:len(data)//2], 2*i, (dim+1)%self.ndim)
        self.__setup(data[len(data)//2+1:], 2*i+1, (dim+1)%self.ndim)

    def __init__(self, data) -> None:
        depth = int(math.log(len(data), 2))+1
        self.size = 2**depth
        self.array = [None] * self.size
        self.ndim = len(data[0])

        self.__setup(data)

    @staticmethod
    def __distance(c1, c2):
        return sum([(a-b)**2 for a, b in zip(c1, c2)])**0.5 
    
    # O(log n)
    def nn(self, other, i=1, exclude_self=False, max_dist=math.inf):
        dist = self.__distance(self.array[i], other)
        if self.size < 2*i+1 or self.array[2*i] is None and self.array[2*i+1] is None:
            if exclude_self and other == self.array[i]:
                return None, math.inf
            else:
                return self.array[i], dist
        
        dim = int(math.log(i, 2))%self.ndim
        ddist = self.array[i][dim] - other[dim]

        cond = self.array[2*i] is None or self.array[2*i+1] is not None and ddist <= 0
        child = 2*i + cond
        ochild = 2*i + 1-cond

        bc, bd = self.nn(other, child, exclude_self=exclude_self, max_dist=max_dist)

        if dist < bd and (not exclude_self or other != self.array[i]):
            bc, bd = self.array[i], dist

        if abs(ddist) < max_dist and self.array[ochild] is not None and abs(ddist) < bd:
            oc, od = self.nn(other, ochild, exclude_self=exclude_self, max_dist=max_dist)
            if od < bd:
                bc, bd = oc, od

        return bc, bd


# n = int(input())

import numpy as np
import time

coords = [tuple(el) for el in np.random.randint(0, 1000000, (100000, 2))]

# for _ in range(n):
    # x, y, z = map(int, input().split())
    # coords.append((x, y, z))

st = time.time()
kdt = KDTree(coords)
print(f"build time: {time.time()-st}")

st = time.time()

bd = math.inf

for coord in coords:
    d = kdt.nn(coord, exclude_self=True, max_dist=bd)[1]

    if d < bd:
        bd = d

print(f"calculation time: {time.time()-st}")
print(bd)