def safe_divide(a, b, max_retries=3):
    attempt = 0
    while attempt < max_retries:
        try:
            result = a / b
            print(f"Success on attempt {attempt + 1}: {a} / {b} = {result}")
            return result
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            attempt += 1
    print("All attempts failed.")
    return None

# Example usage
safe_divide(10, 0)  # Will retry 3 times due to division by zero
safe_divide(10, 2)  # Will succeed on first attempt