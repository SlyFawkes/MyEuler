'''
Created on 9 Dec 2014

@author: vera
'''
#import numpy
import time

with open('resources/p067_triangle.txt') as thing:
    triangles = [[int(digit) for digit in line.split()] for line in thing]
#print array2d

def combineBottomRows(triangleThing):
    triangle = triangleThing
    currentRow = triangle[-1]
    parentRow = triangle[-2]
    for index in xrange(len(parentRow)):
        if currentRow[index] > currentRow[index+1]:
            parentRow[index] += currentRow[index]
        else:
            parentRow[index] += currentRow[index+1]
    del triangles[-1]
    triangles[-1] = parentRow
    

        
def findGreatestPath():
    while len(triangles) > 1:
        combineBottomRows(triangles)
        #print triangles
        
start = time.time()
findGreatestPath()
print triangles
print time.time() - start