
def det_first_prime(number, i):
    while i <= number:
        if number % i == 0:
            print i
            print number/i
            print""
            det_first_prime(number/i, i)
            break
        i += 1


