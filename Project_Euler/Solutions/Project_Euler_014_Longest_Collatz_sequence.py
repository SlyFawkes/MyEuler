'''
Created on 29 Nov 2014

@author: Dean
'''

def collatz(maxNumber):
    numberWithLongestChain = 0
    maxCount = 0
    for item in xrange(2,maxNumber+1):
        currentNumber = item
        count = 0
        while currentNumber > 1:
            if currentNumber%2 == 0:
                currentNumber /= 2
            else:
                currentNumber = (currentNumber*3)+1
            count += 1

        if count > maxCount:
            maxCount = count
            numberWithLongestChain = item
            print numberWithLongestChain
            print maxCount
            print ""
    print numberWithLongestChain

collatz(1000000)
            