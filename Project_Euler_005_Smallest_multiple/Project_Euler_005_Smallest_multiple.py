'''
Created on 24 Nov 2014

@author: dean
'''
primeFactors = []
def detAllPrimes(number, i):
    for item in primeFactors:
        if number%item == 0:
            number = number/item
    while i <= number:
        if number % i == 0:
            primeFactors.append(i)
            detAllPrimes(number/i, i)
            break
        i +=1

def getLCM(n):
    for t in xrange(n+1):
        detAllPrimes(t, 2)
    totalProduct = 1
    for item in primeFactors:
        totalProduct *= item
    print totalProduct

getLCM(20)