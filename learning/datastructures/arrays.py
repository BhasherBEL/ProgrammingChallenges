import numpy as np

class FixedSortedKeys:
    def __init__(self, tup: list[tuple]) -> None:
        self.tuples = tuple(sorted(tup))
        self.length = len(tup)

    def max(self):
        return self.tuples[self.length-1]
    
    def insert(self, *n) -> any:
        deleted = self.tuples[self.length-1]

        if n[0] >= deleted[0]:
            return n

        i = self.__loc(n[0])
        self.tuples = (*self.tuples[:i], n, *self.tuples[i:-1])
                
        return deleted

    def __loc(self, key: any):
        min_ = 0
        max_ = self.length-1
        current = (min_+max_)//2

        while min_ != current != max_:
            if self.tuples[current][0] == key:
                return current
            elif self.tuples[current][0] < key:
                min_ = current
            else:
                max_ = current

            current = (min_+max_)//2
        
        if self.tuples[min_][0] < key:
            return max_
        else:
            return min_

    def __repr__(self) -> str:
        return f'FixedSortedKeys({", ".join(tuple(str(t[0]) + ": " + " ".join(t[1:]) for t in self.tuples))})'

class FixedSortedArray:
    def __init__(self, array: list) -> None:
        self.array = tuple(sorted(array))
        self.length = len(array)

    def max(self):
        return self.array[self.length-1]
    
    def insert(self, n: any) -> any:
        deleted = self.array[self.length-1]

        if n >= deleted:
            return n

        i = self.__loc(n)
        self.array = (*self.array[:i], n, *self.array[i:-1])
                

        return deleted

    def __loc(self, n: any):
        min_ = 0
        max_ = self.length-1
        current = (min_+max_)//2

        while min_ != current != max_:
            if self.array[current] == n:
                return current
            elif self.array[current] < n:
                min_ = current
            else:
                max_ = current
            current = (min_+max_)//2
        
        return max_

    def __repr__(self) -> str:
        return f'FixedSortedArray{self.array}'

if __name__ == "__main__":
    import numpy as np
    fsa = FixedSortedKeys([(1, 'a'), (3, 'c'), (2, 'b')])
    print(fsa)
    fsa.insert(1.5, 'g')
    fsa.insert(0.5, 'g')
    print(fsa)