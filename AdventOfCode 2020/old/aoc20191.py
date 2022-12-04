with open('input20191.txt', 'r') as file:
    data = map(int,filter(lambda x: x.isdigit(), file.read().split('\n')))


t = 0
for el in data:
    if el:
        t += int(el/3)-2

print(t)