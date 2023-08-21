def is_prime(number):
    for element in range(2, number):
        if number % element == 0:
            return False
    return True
