'''
Created on 25 Nov 2014

@author: dean
'''
import time
#@profile
import math
def getTriNumber(n):
    i = 1
    total = 0
    mostFactors = 1
    while mostFactors <n:
        total +=i
        check = getNumOfFactors(total)
        if check > mostFactors:
            mostFactors = check
            print mostFactors
        i += 1
    return total
         
#@profile
def getNumOfFactors(number):
    counter = 2
    y = int(math.sqrt(number))
    for x in xrange(2,y):
        if number%x ==0:
            counter += 2

    return counter
start = time.time()
print getTriNumber(500)
print time.time()-start