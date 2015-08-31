'''
Created on 21 Nov 2014

@author: dean
'''
from time import time


def det_first_prime(number, i):
    while i <= number:
        if number % i == 0:
            print i
            print number/i
            print""
            det_first_prime(number/i, i)
            break
        i += 1

start = time()
det_first_prime(600851475143, 2)
print time() - start
