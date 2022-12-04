import time

def beautiful_int(n: int, sep=' '):
    return '{:,}'.format(n).replace(',', sep)

def experiment(fct, duration=2, **arguments):
    st = et = time.time()
    i = 0
    while et - st < duration:
        fct(**arguments)
        i += 1
        et = time.time()
    print(f'{fct.__name__}: {beautiful_int(int(i/duration))!s} run/s')