
def smallest_multiple(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    unique_prime_factors = []

    for value in xrange(2, n+1):
        for prime in unique_prime_factors:
            if value % prime == 0:
                value = value/prime
        unique_prime_factors.append(value)

    total_product = reduce(lambda x, y: x*y, unique_prime_factors)
    return total_product
