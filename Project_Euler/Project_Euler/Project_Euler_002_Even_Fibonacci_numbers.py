

def fibbonacci(max_value):
    total = 0
    previous_number = 1
    current_number = 2

    while current_number < max_value:

        if current_number % 2 == 0:
            total += current_number

        current_number, previous_number = previous_number+current_number, current_number

    return total
