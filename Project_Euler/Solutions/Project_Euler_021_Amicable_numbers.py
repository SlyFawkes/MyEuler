'''
Created on 9 Dec 2014

@author: vera
'''
from time import time
import math

total = 0
amicable = []
#nonamicable = []

#@profile
def getAllDivisors(number):
    divisors = [1]
    for item in xrange(2, 1 + int(math.sqrt(number))):
        if number%item == 0:
            divisors.append(item)
            if number/item != item:
                divisors.append(number/item)
    return divisors

#@profile
def amicableCheck(number):
    divisorsFirst = getAllDivisors(number)
    totalOfDivisorsFirst = 0
    for item in divisorsFirst:
        totalOfDivisorsFirst += item
    
    divisorsSecond = getAllDivisors(totalOfDivisorsFirst)
    totalOfDivisorsSecond = 0
    for item in divisorsSecond:
        totalOfDivisorsSecond += item
    
    if totalOfDivisorsSecond == number & number != totalOfDivisorsFirst:
        #total += (number + totalOfDivisorsFirst)
        amicable.append(number)
        amicable.append(totalOfDivisorsFirst)
    #===========================================================================
    # else:
    #     nonamicable.append(number)
    #     nonamicable.append(totalOfDivisorsFirst)
    #===========================================================================
        

    
#print getAllDivisors(220)
#print getAllDivisors(284)
start = time()
for item in xrange(1,10000):
    if item not in amicable:
        amicableCheck(item)
for item in amicable:
    total += item
print total
print time() - start
