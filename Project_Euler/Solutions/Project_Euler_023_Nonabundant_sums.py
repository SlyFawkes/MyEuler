'''
Created on 9 Dec 2014

@author: vera
'''

import time, math

#@profile
def getAllDivisors(number):
    divisors = [1]
    for item in xrange(2, 1 + int(math.sqrt(number))):
        if number%item == 0 & item not in divisors:
            divisors.append(item)
            if number/item != item:
                divisors.append(number/item)
    return divisors

#@profile
def checkIfAbundant(number):

    divisors = getAllDivisors(number)
    divisorTotal = 0
    for item in divisors:
        divisorTotal += item
    if divisorTotal > number:
        return True
        
#@profile
def populateAbundantList():
    i = 14
    abundantNumbers = [12]
    for i in xrange(1,28123):
        if checkIfAbundant(i):
            abundantNumbers.append(i)
        i += 1
    print "done"
    return abundantNumbers

#@profile
def checkSum(listNum):
    total = 0
    for i in xrange(1,28123):
        for item in listNum:
            if item >= i:
                total += i
                #print i
                break
            if (i - item) in listNum:
                break
    return total
    

start = time.time()
print checkSum(set(populateAbundantList()))

print time.time() - start