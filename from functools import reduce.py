from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 10, 12]

# Step 1: Double the even numbers
doubled_evens = map(lambda x: x * 2 if x % 2 == 0 else x, numbers)

# Step 2: Filter out numbers < 10
filtered = filter(lambda x: x >= 10, doubled_evens)

# Step 3: Compute the product of remaining numbers
product = reduce(lambda a, b: a * b, filtered, 1)

print(product)
