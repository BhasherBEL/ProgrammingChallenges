from sortedcontainers import SortedDict
import collections


class SortedDefaultDict(SortedDict, collections.defaultdict):
    def __init__(self, defaultvalue, startup=None):
        collections.defaultdict.__init__(self, defaultvalue)
        SortedDict.__init__(self, startup if startup else {})


def generate_dual_dictionary(data: list[tuple[str, str, int]]) -> dict[str, dict[str, int]]:
    out = collections.defaultdict(dict)

    for a, b, dist in data:
        out[a][b] = dist
        out[b][a] = dist

    return dict(out)


graph: dict[str, dict[str, int]] = {
    'K': {
        'M': 4,
        'E': 1,
    },
    'M': {
        'E': 2,
        'H': 2,
    },
    'E': {
        'M': 1,
        'H': 2,
        'F': 1,
    },
    'H': {
        'F': 3,
    },
    'S': {
        'H': 1,
        'F': 2
    }
}

graph2: dict[str, dict[str, int]] = generate_dual_dictionary([
    ('A', 'B', 1),
    ('A', 'C', 2),
    ('B', 'F', 3),
    ('B', 'D', 2),
    ('C', 'D', 3),
    ('D', 'F', 3),
    ('C', 'E', 4),
    ('D', 'E', 2),
    ('D', 'G', 3),
    ('F', 'G', 4),
    ('E', 'G', 5),
])

graph3: dict[str, dict[str, int]] = generate_dual_dictionary([
    ('1', '2', 100),
    ('1', '5', 80),
    ('2', '3', 100),
    ('3', '4', 10),
    ('3', '6', 10),
    ('6', '7', 5),
    ('5', '3', 30)
])

graph4: dict[str, dict[str, int]] = {
    'A': {
        'C': 10,
        'E': 3,
    },
    'B': {
        'C': 4,
        'A': 8,
    },
    'C': {},
    'D': {
        'B': 1,
    },
    'E': {
        'B': 10,
        'D': 2,
    }
}

graph5: dict[str, dict[str, int]] = generate_dual_dictionary([
    ('A', 'B', 2),
    ('A', 'C', 1),
    ('B', 'D', 2),
    ('C', 'E', 4),
    ('C', 'F', 3),
    ('D', 'G', 7),
    ('E', 'F', 1),
    ('E', 'G', 7),
    ('B', 'C', 1)
])


def dijkstra(graph: dict[str, dict[str, int]], origin: str, target: str):  # -> tuple[int, list[tuple[str]]]:
    """Dijkstra algorithm from graph representation

    Args:
        graph (dict[str, dict[str, int]]): Dictionnary of all allowed roads and distances
        origin (str): Origin of the road
        target (str): Destination of the road

    Returns:
        tuple[int, list[tuple[str]]]: Len of sorthests paths and list of possible paths
    """

    if origin == target:
        return (0, [origin])

    candidates = SortedDefaultDict(list)
    for k, v in graph[origin].items():
        candidates[v].append(origin + k)

    visited = {origin}

    print(candidates)

    while target not in ''.join((current := candidates.popitem(0))[1]):
        new_visited = set()
        for path in current[1]:
            if path[-1] not in visited:
                new_visited.add(path[-1])
                for road, distance in graph[path[-1]].items():
                    if road not in visited:
                        candidates[current[0] + distance].append(path + road)
        visited.update(new_visited)
        print(candidates)

    return current[0], [path for path in current[1] if target in path]


print(dijkstra(graph5, 'A', 'G'))
