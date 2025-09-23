class NumberUtils:
    @staticmethod
    def is_even(number):
        return number % 2 == 0

# Example usage
print(NumberUtils.is_even(10))  # True
print(NumberUtils.is_even(7))   # False