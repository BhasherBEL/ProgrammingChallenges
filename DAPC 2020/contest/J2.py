c, e, m = map(int, input().split())

if c == 4 and e%2 == 0 and m <= (e/4)**2 + 1:
    e2 = int(e/2)
    ma = int(e/4)+1
    for i in range(ma):
        j = e2 - i
        if m == i*j:
            print(f'{i+2!s} {j+2!s}', flush=True)
            break
    else:
        print('impossible', flush=True)
else:
    print('impossible', flush=True)