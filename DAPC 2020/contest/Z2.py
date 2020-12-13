import random

n = int(input())

numbers = [int(input()) for _ in range(n)]

if len(set(numbers)) <= 2 or len(numbers) <= 2:
    print('reject', flush=True)
else:
    passed = False
    for i in range(100000):
        random.shuffle(numbers)
        if numbers != sorted(numbers) and numbers != sorted(numbers, reverse=True):
            passed = True
            break
    if passed:
        for n in numbers:
            print(n, flush=True)
    else:
        print('reject', flush=True)