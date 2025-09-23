def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_numbers_up_to(n):
    for i in range(2, n + 1):
        if is_prime(i):
            yield i

# Example usage:
for prime in prime_numbers_up_to(30):
    print(prime)