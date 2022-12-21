import numpy as np

from arrays import FixedSortedKeys

class KDTree:

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
        self.coords = coords
        self.dim = dim
        self.parent = parent
        self.right = right
        self.left = left
        
    def search(self, other, k=1):
        fsa = FixedSortedKeys([(np.inf, None)]*k)
        self.__inner_search(other, fsa)
        return np.array([el[1].coords for el in fsa.tuples])

    def __inner_search(self, other, fsa: FixedSortedKeys):
        KDTree.visited.append(self.coords)

        fsa.insert(self.distance_to_point(other), self)
        
        if self.left is None and self.right is None:
            return

        ddist = self.coords[self.dim] - other[self.dim]

        child = self.left if self.right is None or self.left is not None and ddist <= 0 else self.right
        ochild = self.right if child is self.left else self.left

        child.__inner_search(other, fsa)

        if ochild is not None and abs(ddist) < fsa.max()[0]:
            ochild.__inner_search(other, fsa)

        return

        # if self.left is None and self.right is None:
        #     return self, self.distance_to_point(other)

        # ddist = self.coords[self.dim] - other[self.dim]

        # child = self.left if self.right is None or self.left is not None and ddist <= 0 else self.right
        # ochild = self.right if child is self.left else self.left

        # bc, bd = child.__inner_search(other)
        
        # if (mdist := self.distance_to_point(other)) < bd:
        #     bc, bd = self, mdist
        
        # if ochild is not None and abs(ddist) < bd:
        #     oc, od = ochild.__inner_search(other)
        #     if od < bd:
        #         bc, bd = oc, od

    def distance(self, other):
        return self.distance_to_point(other.coords)

    def distance_to_point(self, coords):
        return self.__distanc_btw(self.coords, coords)

    @staticmethod
    def __distanc_btw(c1, c2):
        return sum([(a-b)**2 for a, b in zip(c1, c2)])**0.5


if __name__ == "__main__":
    import numpy as np
    from matplotlib import pyplot as plt

    n = 1023
    k = 1
    min_ = 0
    max_ = 1000
    data = np.random.randint(min_, max_, [n, k])
    new = np.random.randint(min_, max_, k)

    tree = KDTree.new(data)

    nearest = tree.search(new, 10)

    print(new)
    print(nearest)

    # plt.figure(figsize=(10, 10))
    # plt.scatter(*data.T)
    # plt.scatter(*new.T, color='red')
    # plt.scatter(*np.array(KDTree.visited).T, color='cyan')
    # plt.scatter(*nearest.T, color='orange')
    # plt.ylim(min_, max_)
    # plt.xlim(min_, max_)
    # plt.show()