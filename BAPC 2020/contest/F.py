# TODO
import collections

# n = number of train stations
# m = number of connections between train stations
# p = number of family members
# g = cost by person in a group ticket
n, m, p, g = map(int, input().split())

start_positions = list(map(int, input().split()))

distances = collections.defaultdict(dict)
for i in range(m):
    a, b, c = map(int, input().split())
    distances[a][b] = c
    distances[b][a] = c
    
print(start_positions)