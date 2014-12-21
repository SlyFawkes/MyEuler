'''
Created on 21 Nov 2014

@author: dean
'''

def fibbonacci(maxValue):
    i = 1
    j = 2
    k = 0
    allFibNums = [1,2]
    while k < maxValue:
        allFibNums.append(k)
        k = i+j
        i=j
        j=k
    return allFibNums

def addAllEven(theList):
    total = 0
    for item in theList:
        if item % 2 == 0:
            total += item
    return total

def run(maxValue):
    theList = fibbonacci(maxValue)
    print addAllEven(theList)

run(4000000)
            