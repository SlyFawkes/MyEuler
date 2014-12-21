'''
Created on 21 Nov 2014

@author: dean
'''

def detFirstPrime(number, i):
    while i <= number:
        if number % i == 0:
            print i
            print number/i
            print""
            detFirstPrime(number/i, i)
            break
        i +=1
            
detFirstPrime(600851475143,2)