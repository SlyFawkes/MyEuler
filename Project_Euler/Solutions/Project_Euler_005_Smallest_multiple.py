

def get_unique_primes(number):
    unique_prime_factors = []
    for value in xrange(2, number+1):
        for prime in unique_prime_factors:
            if value % prime == 0:
                value = value/prime
        unique_prime_factors.append(value)
    return unique_prime_factors


def smallest_multiple(n):
    unique_prime_factors = get_unique_primes(n)
    total_product = reduce(lambda x, y: x*y, unique_prime_factors)
    return total_product
