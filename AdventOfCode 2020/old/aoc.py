def search(min_, max_, els, dec, inc):
    for c in els:
        if c == dec:
            max_ = (min_+max_)/2
        elif c == inc:
            min_ = (min_+max_)/2
    return min_

def getid(card):
    l = search(0, 128, card[:7], 'F', 'B')
    c = search(0, 8, card[7:], 'L', 'R')
    return l, c
    

with open('input.txt', 'r') as file:
    cards = file.read().split('\n')
    
plane = [[0]*8 for __ in range(128)]

for card in cards:
    l, c = map(int, getid(card))
    plane[l][c] = 1
    
for i, l in enumerate(plane):
    for j, c in enumerate(l):
        if not c:
            print(i,j, i*8+j)