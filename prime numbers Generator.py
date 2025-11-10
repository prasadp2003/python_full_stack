def prime_generator(n):
    for num in range(2, n + 1):  # Start from 2, the first prime
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):  # Check divisibility up to sqrt(num)
            if num % i == 0:
                is_prime = False
                break  # Exit inner loop early if not prime
        if is_prime:
            yield num
            
            for prime in prime_generator(50):
    print(prime, end=' ')