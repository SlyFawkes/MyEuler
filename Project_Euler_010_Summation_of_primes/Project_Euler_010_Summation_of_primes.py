'''
Created on 24 Nov 2014

@author: dean
'''

import time

#@profile
def findAllPrimesBelow(k):
    primes = [2, 3]

    t = 2
    j = primes[-1] + 2

    while j < k:
        u=1
        while u < t:
            p = primes[u]
            if j%p == 0:
                j +=2
                u = 1
            elif p**2 > j:
                break
            else:
                u+=1

        primes.append(j)
        j += 2
        t += 1
    primes.pop()
    return primes


start = time.time()
primes = findAllPrimesBelow(1000)
total = 0
for item in primes:
    total += item
print total
end = time.time()
print end - start