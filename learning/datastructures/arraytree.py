class SegmentTree(object):
    def __init__(self, data, fct, default=0) -> None:
        self.array = [default] * (len(data) * 2)
        self.fct = fct
        self.len = len(data)
        for i, el in enumerate(data):
            self.array[self.len + i] = el
        
        for i in range(self.len - 1, 0, -1):
            self.array[i] = fct(self.array[2*i], self.array[2*i+1])

    def get(self, i, j):
        i += self.len
        j += self.len
        res = 0
        while i < j:
            if i&1:  # i%2 == 1
                res += self.array[i]
                i += 1 
            if j&1:  # j%2 == 1
                j -= 1
                res += self.array[j]
            i >>= 1  # i //= 2
            j >>= 1  # j //= 2
        return res

from math import log
import random

visited = []

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
        depth = int(log(len(data), 2))+1
        self.size = 2**depth
        self.array = [None] * self.size
        self.ndim = len(data[0])

        self.__setup(data)

    @staticmethod
    def __distance(c1, c2):
        return sum([(a-b)**2 for a, b in zip(c1, c2)])**0.5 
    
    # O(log n)
    def nn(self, other, i=1):
        visited.append(self.array[i])
        dist = self.__distance(self.array[i], other)
        if self.size < 2*i+1 or self.array[2*i] is None and self.array[2*i+1] is None:
            return self.array[i], dist
        
        dim = int(log(i, 2))%self.ndim
        ddist = self.array[i][dim] - other[dim]

        cond = self.array[2*i] is None or self.array[2*i+1] is not None and ddist <= 0
        child = 2*i + cond
        ochild = 2*i + 1-cond

        bc, bd = self.nn(other, child)

        if dist < bd:
            bc, bd = self.array[i], dist
        
        if self.array[ochild] is not None and abs(ddist) < bd:
            oc, od = self.nn(other, ochild)
            if od < bd:
                bc, bd = oc, od

        return bc, bd

if __name__ == "__main__":
    import numpy as np
    from matplotlib import pyplot as plt
    import time

    data = np.random.randint(0, 10000, (100000, 2))

    st = time.time()
    kdt = KDTree(data)
    print(f'setup time: {time.time()-st:.3g}s')

    st = time.time()
    for target in np.random.randint(0, 10000, (2, 1000000)):
        nn, d = kdt.nn(target)
    print(f'NN time: {time.time()-st:.3g}s')

    # plt.figure(figsize=(10, 10))
    # plt.scatter(*data.T)
    # plt.scatter(*np.array(visited).T, color='cyan')
    # plt.scatter(*target, color='red')
    # plt.scatter(*nn, color='orange')
    # plt.show()
