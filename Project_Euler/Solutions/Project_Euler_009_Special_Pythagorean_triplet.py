
def euclid_variables():
    for n in xrange(1, 500):
        for m in xrange(1, int(500**0.5)):
            if m*(m+n) == 500:
                return m, n


def special_pythagorean_triplet():
    numbers = euclid_variables()
    a = numbers[0]**2-numbers[1]**2
    b = 2*numbers[0]*numbers[1]
    c = numbers[1]**2 + numbers[0]**2
    return a*b*c
