'''
Created on 24 Nov 2014

@author: dean
'''
def sumOfSquares(n):
    total = 0
    for i in xrange(n+1):
        total += i**2
    return total

def squareOfSum(n):
    total = 0
    for i in xrange(n+1):
        total += i
    return total**2

def differenceInSquares(n):
    print squareOfSum(n) - sumOfSquares(n)
    
differenceInSquares(1000)