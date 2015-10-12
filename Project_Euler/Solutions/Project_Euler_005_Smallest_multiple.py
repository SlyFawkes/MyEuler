
primeFactors = []


def det_all_primes(number, i):
    for item in primeFactors:
        if number % item == 0:
            number = number/item
    while i <= number:
        if number % i == 0:
            primeFactors.append(i)
            det_all_primes(number/i, i)
            break
        i += 1


def smallest_multiple(n):
    for t in xrange(n+1):
        det_all_primes(t, 2)
    total_product = 1
    for item in primeFactors:
        total_product *= item
    return total_product
