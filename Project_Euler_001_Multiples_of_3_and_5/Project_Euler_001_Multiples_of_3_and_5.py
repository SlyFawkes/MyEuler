from time import time


def run(n):
    total = 0
    for x in range(n):
        if x % 5 == 0 or x % 3 == 0:
            total += x
    return total

start = time()
print run(1000)
print time() - start
