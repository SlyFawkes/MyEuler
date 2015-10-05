'''
Created on 21 Nov 2014

@author: dean
'''


def fibbonacci(max_value):
    i = 1
    j = 2
    k = 0
    all_fib_nums = [1, 2]
    while k < max_value:
        all_fib_nums.append(k)
        k = i+j
        i = j
        j = k
    return all_fib_nums


def add_all_even(the_list):
    total = 0
    for item in the_list:
        if item % 2 == 0:
            total += item
    return total


def run(max_value):
    the_list = fibbonacci(max_value)
    print add_all_even(the_list)

run(4000000)
