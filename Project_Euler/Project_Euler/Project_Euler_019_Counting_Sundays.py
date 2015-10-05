'''
Created on 9 Dec 2014

@author: vera
'''
import datetime, time

start = time.time()
total = 0
workingDate = datetime.date(1901, 1, 1)
while workingDate.year <= 2000:
    if workingDate.weekday() == 6:
        total +=1
    if workingDate.month == 12:
        workingDate = workingDate.replace(year=workingDate.year+1)
        workingDate = workingDate.replace(month=1)
    else:
        workingDate = workingDate.replace(month=workingDate.month+1)
    #print workingDate.month

print total
print time.time() - start