'''
Created on 12 Dec 2014

@author: vera
'''
from time import time

def findFirstFibNumber(length):
    prev = 1
    current = 1
    term = 2
    while len(str(current)) < length:
        term += 1
        x = prev
        prev = current
        current = prev + x
    print term

start = time()
findFirstFibNumber(1000)
print time() - start