'''
Created on 12 Dec 2014

@author: vera
'''

import time

primesList = [2, 3]

def findAllPrimesBelow(k, primesList):
    primes = primesList

    t = 2
    j = 3

    while j < k:
        j += 2
        u=1
        while u < t:

            if j%primes[u] == 0:
                j +=2
                u = 1
            elif primes[u]**2 > j:
                print j
                break
            else:
                u+=1

        primes.append(j)
        print j
        t += 1
    primes.pop()
    primesList = primes
    if j == k:
        print j
        return True


def checkIfPrime(number):
    if number in set(primesList):
        return True
    else:
        findAllPrimesBelow(number, primesList)


print findAllPrimesBelow(20, primesList)
print primesList



