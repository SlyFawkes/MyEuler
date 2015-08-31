'''
Created on 21 Nov 2014

@author: dean
'''

listOfNumbers = []


def multiple3(n):
    i = 0
    while i < n:
        
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


def add_list_numbers():
    total = 0
    for item in listOfNumbers:
        total += item
    return total


def run(n):
    multiple3(n)
    multiple5(n)
    print add_list_numbers()
    
run(1000)
