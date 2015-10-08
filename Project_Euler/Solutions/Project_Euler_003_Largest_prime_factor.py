
def largest_prime_factor(number):
    divisor = 2
    while divisor <= number/2:
        if number % divisor == 0:
            number /= divisor
        else:
            divisor += 1
    return number



