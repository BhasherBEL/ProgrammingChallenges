# Wrong answer
n, p = map(int, input().split())

solved = []
I = p

last = 0
for i in range(n):
    curr = int(input())
    if solved and curr < last:
        I -= 1
    solved.append(I)
    last = curr
    
if I == 0 or I == 1 and last > 0:
    for s in solved:
        print(s, flush=True)
else:
    print('ambigous', flush=True)