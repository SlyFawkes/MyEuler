

def largest_palindrome(n):
    largest = 0
    for i in xrange(10**(n-1), 10**n):
        for j in xrange(10**(n-1), 10**n):
            number_to_check = i*j
            if number_to_check > largest and check_if_palindrome(number_to_check):
                largest = number_to_check
    return largest


def check_if_palindrome(to_check):
    string_to_check = str(to_check)
    if string_to_check[::-1] == string_to_check:
        return True

