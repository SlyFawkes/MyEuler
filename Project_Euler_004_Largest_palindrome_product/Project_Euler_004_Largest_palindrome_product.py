'''
Created on 21 Nov 2014

@author: dean
'''


def multiply_all_n_length_numbers(n):
    all_multiplies = []
    for i in xrange(10**n,10**(n+1)):
        for j in xrange(10**n, 10**(n+1)):
            all_multiplies.append(str(i*j))
    return all_multiplies
    # ===========================================================================
    # for thing in all_multiplies:
    #     print thing
    # ===========================================================================


def check_if_palindrome(list_of_numbers):
    all_palindromes = []
    for item in list_of_numbers:
        if item[::-1] == item:
            all_palindromes.append(item)
    return all_palindromes


def sort_array(array_to_be_sorted):
    array_to_be_sorted.sort(key=int)
    return array_to_be_sorted
        
allMultiples = multiply_all_n_length_numbers(2)
unsortedList = check_if_palindrome(allMultiples)
sortedList = sort_array(unsortedList)

for item in sortedList:
    print item
