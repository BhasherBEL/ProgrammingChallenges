with open('input1.txt', 'r') as file:
    data = list(map(int, file.read().split('\n')))
    
r = 0
v = 0
for a in data:
    for b in data:
        for c in data:
            if a + b + c== 2020:
                print(a, b, c, a*b*c)