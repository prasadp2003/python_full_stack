def multi_type_sort(mixed_list):
    """
    Sorts a list containing mixed types (integers, floats, and strings).

    The sorting criteria are:
    1. All numbers (int or float) come before all strings.
    2. Numbers are sorted numerically (ascending).
    3. Strings are sorted alphabetically (ascending).

    Args:
        mixed_list (list): The list containing a mix of numbers and strings.

    Returns:
        list: The sorted list.
    """

    def custom_sort_key(item):
        """
        Custom key function used by sorted().

        The return value is a tuple (priority, value).
        Priority 0 is for numbers, Priority 1 is for strings.
        This ensures all priority 0 items come before priority 1 items.
        The second element in the tuple (the item itself) handles the
        secondary sorting within the priority group (numerical or alphabetical).
        """
        if isinstance(item, (int, float)):
            # Priority 0 for numbers
            # We use the item itself as the secondary sort key for numerical order
            return (0, item)
        elif isinstance(item, str):
            # Priority 1 for strings
            # We use the item itself as the secondary sort key for alphabetical order
            return (1, item)
        else:
            # Handle other types by placing them last, e.g., using Priority 2
            # or raising an error if unexpected types are strictly forbidden.
            # For simplicity, we'll place unknown types last, sorted by string representation.
            return (2, str(item))

    # Use the built-in sorted() function with the custom key
    return sorted(mixed_list, key=custom_sort_key)

# Demonstration
if __name__ == "__main__":
    example_list = [
        "apple", 3.14, "banana", 10, -5, "cherry", 0, 10.5, "date", 1
    ]

    print(f"Original List: {example_list}")

    sorted_list = multi_type_sort(example_list)

    print(f"Sorted List:   {sorted_list}")

    # Another example
    another_list = [
        "Zebra", 100, "Ant", 0.5, 25, "dog", "Cat", 99.99
    ]

    print("\n--- Second Example ---")
    print(f"Original List: {another_list}")

    sorted_list_2 = multi_type_sort(another_list)

    print(f"Sorted List:   {sorted_list_2}")