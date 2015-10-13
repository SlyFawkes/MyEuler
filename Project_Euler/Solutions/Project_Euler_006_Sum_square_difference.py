
def sum_of_squares(n):
    total = 0
    for i in xrange(n+1):
        total += i**2
    return total


def square_of_sum(n):
    total = 0
    for i in xrange(n+1):
        total += i
    return total**2


def sum_square_difference(n):
    return square_of_sum(n) - sum_of_squares(n)
