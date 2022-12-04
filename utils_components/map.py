from __future__ import annotations
from enum import Enum
import numpy as np


class Map:
    class NeighboursType(Enum):
        CROSS = 0
        ALL = 1

    @staticmethod
    def get_neighbours(tup: tuple, /, dist: int = 1, type: NeighboursType = NeighboursType.CROSS, exclude=True, dimensions: None | tuple = None, cycle=False) -> tuple | int:
        """
        Get the neighbours coordinates.

        :param tup: initial coordinate.
        :param dist: maximum distance of neighbours.
        :param type: CROSS (Only direct neighbours) or ALL (also in diagonal).
        :param exclude: Exclude initial coordinate from the result.
        :param dimensions: Borders of the map.
        :param cycle: If the map is circular.
        :return: a generator of neighbours.
        """
        if dimensions and len(tup) != len(dimensions):
            raise ValueError('Borders and tuple have different dimensions')
        for i in range(-dist, dist+1):
            current = tup[0]
            next_ = tup[1:]
            if dimensions and current + i < dimensions[0][0]:
                if cycle:
                    current += dimensions[0][1]-dimensions[0][0]
                else:
                    continue
            elif dimensions and current + i > dimensions[0][1]:
                if cycle:
                    current += dimensions[0][0]-dimensions[0][1]
                else:
                    continue

            if len(next_) == 0:
                yield current+i,
            else:
                for co in Map.get_neighbours(next_, dist, type=type, exclude=False, dimensions=(None if dimensions is None else dimensions[1:]), cycle=cycle):
                    res = current+i, *co
                    if exclude and (current, *next_) == res or type == Map.NeighboursType.CROSS and \
                            (not cycle and Map.coordinates_distance(res, (current, *next_), type=type) > dist or
                             cycle and Map.cycle_coordinates_distance(res, (current, *next_), dimensions=dimensions) > dist):
                        continue

                    yield res

    @staticmethod
    def coordinates_distance(t1: tuple, t2: tuple, /, type: NeighboursType = NeighboursType.CROSS) -> int | float:
        """
        Get distance between two coordinates.
        :param t1:
        :param t2:
        :param type:
        :return:
        """
        if type == Map.NeighboursType.CROSS:
            return sum(abs(x1 - x2) for x1, x2 in zip(t1, t2))
        elif type == Map.NeighboursType.ALL:
            return sum((x1 - x2)**2 for x1, x2 in zip(t1, t2))**0.5

    @staticmethod
    def cycle_coordinates_distance(t1, t2, dimensions):
        """
        Get distance between two coordinates, but in a circular map.
        :param t1:
        :param t2:
        :param dimensions:
        :return:
        """
        if len(t1) == 0 or len(t2) == 0:
            return 0
        return min(
            abs(t1[0]-t2[0]),
            abs(t1[0]-t2[0]+dimensions[0][1]-dimensions[0][0]),
            abs(t1[0]-t2[0]+dimensions[0][0]-dimensions[0][1]),
        ) + Map.cycle_coordinates_distance(t1[1:], t2[1:], dimensions[1:])

    @staticmethod
    def path(t1, t2):
        p1 = np.array(t1)
        p2 = np.array(t2)

        step = (p2-p1)/max(abs(p2-p1))

        steps = []
        for i in range(max(abs(p2-p1))+1):
            cs = p1 + 0.5 + i*step
            steps.append([int(el) for el in cs])

        return np.array(steps)
