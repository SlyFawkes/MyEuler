'''
Created on 9 Dec 2014

@author: vera
'''

from math import factorial

def addDigitsOfNum(number):
    strNumber = str(number)
    total = 0
    for char in strNumber:
        total += int(char)
    print total

addDigitsOfNum(factorial(100))