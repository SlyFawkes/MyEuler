'''
Created on 8 Dec 2014

@author: vera
'''

def addDigitsOfNum(number):
    strNumber = str(number)
    total = 0
    for char in strNumber:
        total += int(char)
    print total

addDigitsOfNum(2**1000)