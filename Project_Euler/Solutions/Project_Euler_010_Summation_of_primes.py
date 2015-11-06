
def find_all_primes_below(k):
    prime_list = [2, 3]

    t = 2
    j = prime_list[-1] + 2

    while j < k:
        u = 1
        while u < t:
            p = prime_list[u]
            if j % p == 0:
                j += 2
                u = 1
            elif p**2 > j:
                break
            else:
                u += 1

        prime_list.append(j)
        j += 2
        t += 1
    prime_list.pop()
    return prime_list


def summation_of_primes(n):
    primes = find_all_primes_below(n)
    total = 0
    for item in primes:
        total += item
    return total
