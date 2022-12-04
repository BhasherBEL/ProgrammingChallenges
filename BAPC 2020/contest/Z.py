import random

n = int(input())

numbers = [int(input()) for _ in range(n)]

if len(set(numbers)) <= 2 or len(numbers) <= 2:
    print('reject', flush=True)
else:
    numbers.sort()
    i = 2
    while numbers[i] == numbers[0]:
        i += 1
    if numbers[0] == numbers[i]:
        print('reject', flush=True)
    else:
        # print('--', i)
        numbers[1], numbers[i] = numbers[i], numbers[1]
        for number in numbers:
            print(number, flush=True)