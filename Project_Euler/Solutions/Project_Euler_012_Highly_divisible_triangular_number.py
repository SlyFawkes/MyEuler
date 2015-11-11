import math


def get_tri_number(n):
    i = 1
    total = 0
    most_factors = 1
    while most_factors < n:
        total += i
        check = get_num_of_factors(total)
        if check > most_factors:
            most_factors = check
            print most_factors
        i += 1
    return total


def get_num_of_factors(number):
    counter = 2
    y = int(math.sqrt(number))
    for x in xrange(2, y):
        if number % x == 0:
            counter += 2

    return counter

print get_tri_number(500)
