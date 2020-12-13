# Wrong answer
n, p = map(int, input().split())

solved = [p]
current = p
current_time = int(input().strip())
for i in range(1, n):
    t = int(input().strip())
    if t < current_time and current_time != 0:
        current -= 1
    elif current_time == 0 and t > current_time:
        current = -1
        break
    current_time = t
    solved.append(current)

if current != 0:
    print('ambiguous', flush=True)
else:
    for sol in solved:
        print(sol, flush=True)