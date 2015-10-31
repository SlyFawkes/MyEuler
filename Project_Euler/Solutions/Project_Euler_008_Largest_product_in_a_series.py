

def biggest_adj_product(number_as_string, length):
    if length <= 0:
        return 0

    largest = 0

    for i in xrange(len(number_as_string)-length+1):
        current = number_as_string[i: i+length]
        total = 1

        for j in xrange(length):
            total *= int(current[j])

        largest = max(largest, total)

    return largest
