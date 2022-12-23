import numpy as np

from arrays import FixedSortedKeys

class BinaryTree(object):
    def __init__(self, key=None, value=None, left=None, right=None, name=None) -> None:
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        self.name = self.__class__.__name__ if name is None else name

    def __repr__(self) -> str:
        res = f"{self.name}(key={self.key}"
        if self.value:
            res += f", value={self.value}"
        if self.left is not None:
            res += f", left={self.left}"
        if self.right is not None:
            res += f", right={self.right}"
        return res + ')'


class KDTree(BinaryTree):
    visited = []

    @staticmethod
    def new(data, curr_dim=0):
        if not len(data):
            return None
        n_dim = len(data[0]);
        data = sorted(data, key=lambda x: x[curr_dim])
        tree = KDTree(
            coords=data[len(data)//2],
            dim=curr_dim,
            parent=None,
            right=KDTree.new(data[:len(data)//2], (curr_dim+1) % n_dim),
            left=KDTree.new(data[len(data)//2+1:], (curr_dim+1) % n_dim)
        )
        if tree.right:
            tree.right.parent = tree
        if tree.left:
            tree.left.parent = tree
        return tree
    
    def __init__(self, coords, dim, parent=None, right=None, left=None):
        super().__init__(coords, None, left, right)
        self.dim = dim
        self.parent = parent
        
    def knn(self, other, k=1):
        fsa = FixedSortedKeys([(np.inf, None)]*k)
        self.__inner_knn(other, fsa)
        return np.array([el[1].key for el in fsa.tuples])

    def __inner_knn(self, other, fsa: FixedSortedKeys):
        KDTree.visited.append(self.key)

        fsa.insert(self.distance_to_point(other), self)
        
        if self.left is None and self.right is None:
            return

        ddist = self.key[self.dim] - other[self.dim]

        child = self.left if self.right is None or self.left is not None and ddist <= 0 else self.right
        ochild = self.right if child is self.left else self.left

        child.__inner_knn(other, fsa)

        if ochild is not None and abs(ddist) < fsa.max()[0]:
            ochild.__inner_knn(other, fsa)

        return

        # if self.left is None and self.right is None:
        #     return self, self.distance_to_point(other)

        # ddist = self.key[self.dim] - other[self.dim]

        # child = self.left if self.right is None or self.left is not None and ddist <= 0 else self.right
        # ochild = self.right if child is self.left else self.left

        # bc, bd = child.__inner_knn(other)
        
        # if (mdist := self.distance_to_point(other)) < bd:
        #     bc, bd = self, mdist
        
        # if ochild is not None and abs(ddist) < bd:
        #     oc, od = ochild.__inner_knn(other)
        #     if od < bd:
        #         bc, bd = oc, od
        
        # return bc, bd

    def distance(self, other):
        return self.distance_to_point(other.key)

    def distance_to_point(self, other):
        return self.__distanc_btw(self.key, other)

    @staticmethod
    def __distanc_btw(c1, c2):
        return sum([(a-b)**2 for a, b in zip(c1, c2)])**0.5 
    
class SegmentTree(BinaryTree):
    @staticmethod
    def new(data, fct, start=0, end=None):
        if end is None:
            end = len(data)-1

        tree = SegmentTree(
            from_=start,
            to=end,
            left=SegmentTree.new(data, start, (start+end)//2, fct) if start != end else None,
            right=SegmentTree.new(data, (start+end)//2+1, end, fct) if start != end else None,
            fct=fct
        ) 

        if start == end:
            tree.value = data[start]
        else:
            tree.value = fct(tree.left.value, tree.right.value)
        
        return tree
        

    def __init__(self, from_, to, value=None, left=None, right=None, fct=None) -> None:
        super().__init__(key=(from_, to), value=value, left=left, right=right)
        self.fct = fct

    def get(self, i, j):
        if i == self.key[0] and j == self.key[1]:
            return self.value
        
        if i >= self.right.key[0]:
            return self.right.get(i, j)
        if j <= self.left.key[1]:
            return self.left.get(i, j)
        
        return self.fct(self.left.get(i, self.left.key[1]), self.right.get(self.right.key[0], j))
            

if __name__ == "__main__":
    tree = SegmentTree.new([2, 3, -1, 5, -2, 4, 8, 10], fct=min)

    print([2, 3, -1, 5, -2, 4, 8, 10])
    print(tree)
    print(tree.get(0, 6))