'''
Created on 24 Nov 2014

@author: dean
'''

def specialTriplet():
    for n in xrange(1,500):
        for m in xrange(1,500):
            if m*(m+n) == 500:
                return m, n
                
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

detAllPrimes(500, 2)
numbers = specialTriplet()
a = numbers[0]**2-numbers[1]**2
b = 2*numbers[0]*numbers[1]
c = numbers[1]**2 + numbers[0]**2
print a,b,c

print a*b*c