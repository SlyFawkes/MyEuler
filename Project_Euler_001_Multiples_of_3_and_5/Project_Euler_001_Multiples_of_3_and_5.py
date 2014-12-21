'''
Created on 21 Nov 2014

@author: dean
'''

listOfNumbers = []

def multiple3(n):
    i = 0
    while i < 1000:
        
        if i not in listOfNumbers:
            listOfNumbers.append(i)
            print i
        i += 3
        
        
def multiple5(n):
    j = 0
    while j < 1000:
        
        if j not in listOfNumbers:
            listOfNumbers.append(j)
            print j
        j += 5

def addListNumbers():
    total = 0
    for item in listOfNumbers:
        total += item
    return total

def run(n):
    multiple3(n)
    multiple5(n)
    print addListNumbers()
    
run(1000)