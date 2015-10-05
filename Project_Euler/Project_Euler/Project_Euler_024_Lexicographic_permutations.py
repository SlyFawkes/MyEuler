'''
Created on 11 Dec 2014

@author: vera
'''


import itertools
from time import time
start = time()
#@profile
def doTheThing():
    i = 0
    listNum = itertools.permutations("0123456789")
    for item in listNum:
        i += 1
        if i == 1000000:
            for thing in item:
                print thing
            return

doTheThing()
print time()-start