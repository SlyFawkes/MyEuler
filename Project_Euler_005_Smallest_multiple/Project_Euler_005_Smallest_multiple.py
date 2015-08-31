'''
Created on 24 Nov 2014

@author: dean
'''
primeFactors = []


def det_all_primes(number, i):
    for item in primeFactors:
        if number%item == 0:
            number = number/item
    while i <= number:
        if number % i == 0:
            primeFactors.append(i)
            det_all_primes(number/i, i)
            break
        i += 1


def get_lcm(n):
    for t in xrange(n+1):
        det_all_primes(t, 2)
    total_product = 1
    for item in primeFactors:
        total_product *= item
    print total_product

get_lcm(20)
