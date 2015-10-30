
def find_nth_prime(nth_prime):

    if nth_prime == 1:
        return 2
    elif nth_prime < 1:
        return 0

    primes_list = [2, 3]
    check_if_prime = 5
    list_length = 2
    offset = 2

    while list_length < nth_prime:

        for prime in primes_list:

            if check_if_prime % prime == 0:
                break

            elif prime**2 > check_if_prime:
                primes_list.append(check_if_prime)
                list_length += 1
                break

        check_if_prime += offset
        offset = 6 - offset

    return primes_list[-1]

