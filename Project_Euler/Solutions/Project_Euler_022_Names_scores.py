'''
Created on 9 Dec 2014

@author: vera
'''


with open('resources/p022_names.txt') as thing:
    names = thing.read().split(',')

names.sort()

def getValue(char):
    charV = ord(char)
    if 65 <= charV <= 90:
        # Upper case letter
        return charV - 64

total = 0

for index,item in enumerate(names):
    nameTotal = 0
    letterPos = 1
    while letterPos < len(item) - 1:
        nameTotal += getValue(item[letterPos])
        letterPos += 1
    total += nameTotal*(index+1)

print total