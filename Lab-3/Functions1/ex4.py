def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):
    return list(filter(lambda x: is_prime(x), numbers))

print(filter_prime([1, 2, 3, 4, 5, 17, 19, 20]))