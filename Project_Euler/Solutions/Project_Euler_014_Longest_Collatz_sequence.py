
def collatz(max_number):
    number_with_longest_chain = 0
    max_count = 0
    for item in xrange(2, max_number+1):
        current_number = item
        count = 0
        while current_number > 1:
            if current_number % 2 == 0:
                current_number /= 2
            else:
                current_number = (current_number*3)+1
            count += 1

        if count > max_count:
            max_count = count
            number_with_longest_chain = item
            print number_with_longest_chain
            print max_count
            print ""
    print number_with_longest_chain

collatz(1000000)
