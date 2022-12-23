import random

def selection(lst, k):
    p = random.choice(lst)
    L = [el for el in lst if el <= p]

    if k == len(L):
        return p
    
    if k < len(L):
        L.remove(p)
        return selection(L, k)
    
    R = [el for el in lst if el > p]
    return selection(R, k-len(L))

def median(lst):
    return selection(lst, len(lst)//2)

print(selection([1, 4, 6, 2, 8, 9, 10, 6, 5, 12, 0, -2], 2))
print(median([]))
