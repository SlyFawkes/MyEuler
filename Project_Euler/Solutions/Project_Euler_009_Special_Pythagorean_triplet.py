
def euclid_variables(upper_limit):
    for n in xrange(1, upper_limit):
        for m in xrange(1, int(upper_limit**0.5)):
            if m*(m+n) == upper_limit:
                return m, n


def special_pythagorean_triplet():
    numbers = euclid_variables(500)
    a = numbers[0]**2-numbers[1]**2
    b = 2*numbers[0]*numbers[1]
    c = numbers[1]**2 + numbers[0]**2
    return a*b*c
