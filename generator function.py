def even_numbers_up_to(n):
    for i in range(2, n + 1, 2):
        yield i

# Example usage:
for num in even_numbers_up_to(10):
    print(num)