with open('input2.txt', 'r') as file:
    data = file.read().split('\n')
    
v = 0
iv = 0
for line in data:
    if line.count(' ') != 2:
        continue
    r, l, p = line.split(' ')
    min_, max_ = map(int, r.split('-'))
    min_ -= 1
    max_ -= 1
    l = l.replace(':', '')
    if (len(p) > max_ and ((p[min_] == l) ^ (p[max_] == l))) or (min_ < len(p) < max_ and p[min_] == l):
        v += 1
    else:
        # print(r,l,p)
        iv += 1
        
print(v, iv)
        