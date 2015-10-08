

def total_multiples(n):
    total = 0
    for x in xrange(n):
        if x % 3 == 0 or x % 5 == 0:
            total += x
    return total
