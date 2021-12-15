import sortedcontainers
from collections import defaultdict


class Graph:
    @staticmethod
    def __a_star_reconstruct_path(came_from, current):
        path = [current]
        while current in came_from:
            current = came_from[current]
            path.insert(0, current)
        return path

    @staticmethod
    def a_star(start, goal, estimate, weight, get_neighbours):
        open_set = sortedcontainers.SortedDict({estimate(start, goal): [start]})
        came_from = {}

        # known
        g_score = defaultdict(lambda: float('inf'))
        g_score[start] = 0

        while open_set:
            for current in open_set.popitem(0)[1]:

                if current == goal:
                    return Graph.__a_star_reconstruct_path(came_from, current)

                for neighbour in get_neighbours(current):
                    tentative = g_score[current] + weight(current, neighbour)

                    if tentative < g_score[neighbour]:
                        came_from[neighbour] = current
                        g_score[neighbour] = tentative

                        estimation = tentative + estimate(current, goal)

                        open_set.setdefault(estimation, list())
                        open_set[estimation].append(neighbour)