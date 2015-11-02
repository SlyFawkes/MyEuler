
def special_triplet():
    for n in xrange(1, 500):
        for m in xrange(1, 500):
            if m*(m+n) == 500:
                return m, n
                
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

det_all_primes(500, 2)
numbers = special_triplet()
a = numbers[0]**2-numbers[1]**2
b = 2*numbers[0]*numbers[1]
c = numbers[1]**2 + numbers[0]**2
print a, b, c

print a*b*c
