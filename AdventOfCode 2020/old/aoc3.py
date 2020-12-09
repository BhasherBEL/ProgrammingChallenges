with open('input3.txt', 'r') as file:
    data = [list(el) for el in file.read().split('\n')]

def check(dx, dy):
    x = 0
    y = 0
    tree = 0
    ntree = 0
    while y < len(data)-dy:
        y += dy
        x = (x + dx) % len(data[y])
        if data[y][x] == '#':
            tree += 1
        else:
            ntree += 1
    return tree

        
print(check(3, 1) * check(1, 1) * check(5, 1) * check(7, 1) * check(1, 2))