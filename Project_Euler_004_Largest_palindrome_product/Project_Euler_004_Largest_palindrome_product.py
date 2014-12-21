'''
Created on 21 Nov 2014

@author: dean
'''


def multiplyAllNLengthNumbers(n):
    allMultiplies = []
    for i in xrange(10**n,10**(n+1)):
        for j in xrange(10**n, 10**(n+1)):
            allMultiplies.append(str(i*j))
    return allMultiplies
    #===========================================================================
    # for thing in allMultiplies:
    #     print thing
    #===========================================================================
        
def checkIfPalindrome(listOfNumbers):
    allPalindromes = []
    for item in listOfNumbers:
        if item[::-1] == item:
            allPalindromes.append(item)
    return allPalindromes
            
def sortArray(arrayToBeSorted):
    arrayToBeSorted.sort(key=int)
    return arrayToBeSorted
        
allMultiples = multiplyAllNLengthNumbers(2)
unsortedList = checkIfPalindrome(allMultiples)
sortedList = sortArray(unsortedList)

for item in sortedList:
    print item