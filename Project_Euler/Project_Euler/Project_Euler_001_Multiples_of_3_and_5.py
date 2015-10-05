from time import time


def total_multiples(n):
    total = 0
    for x in xrange(n):
        if x % 5 == 0 or x % 3 == 0:
            total += x
    return total

start = time()
print total_multiples(1000)
print time() - start
