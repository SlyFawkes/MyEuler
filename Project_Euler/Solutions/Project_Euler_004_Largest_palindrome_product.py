

def largest_palindrome(n):
    largest = 0
    for i in xrange(10**n, 10**(n-1), -1):
        for j in xrange(i, 10**(n-1), -1):
            number_to_check = i*j
            if number_to_check < largest:
                break
            if check_if_palindrome(number_to_check):
                largest = number_to_check
    return largest


def check_if_palindrome(to_check):
    string_to_check = str(to_check)
    if string_to_check[::-1] == string_to_check:
        return True

