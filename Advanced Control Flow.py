"""
Function demonstrating advanced control flow (continue and break) 
within a list processing loop.
"""

def process_list_with_rules(data_list):
    """
    Processes a list of numbers, applying the following custom rules:
    1. Skip: If a number is a multiple of 3 (number % 3 == 0), it is skipped 
       and not added to the result list (using 'continue').
    2. Break: If a number is greater than 100, the processing stops 
       immediately (using 'break'), and no further numbers are checked.

    Args:
        data_list (list): The list of numbers to process.

    Returns:
        list: A new list containing only the numbers that passed the rules.
    """
    result = []
    
    print(f"--- Starting processing for list: {data_list}")
    
    for number in data_list:
        # Rule 2: BREAK condition - Stop processing if number is too large
        if number > 100:
            print(f"BREAK: Encountered {number}. Stopping processing immediately.")
            break  # Exit the entire for loop
        
        # Rule 1: SKIP condition - Skip multiples of 3
        if number % 3 == 0:
            print(f"CONTINUE: Skipping {number} (multiple of 3).")
            continue # Skip the rest of the current loop iteration
        
        # If the number passes both checks, it is appended
        print(f"PASS: Adding {number} to the result.")
        result.append(number)
        
    print("--- Processing finished.\n")
    return result

# --- Example Usage ---

# Example 1: Demonstrates both 'continue' and normal flow
list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
result_a = process_list_with_rules(list_a)
print(f"Final Result A: {result_a}")
# Expected: [1, 2, 4, 5, 7, 8, 10, 11] (3, 6, 9 skipped)

print("-" * 30)

# Example 2: Demonstrates 'break'
list_b = [10, 20, 30, 40, 101, 50, 60]
result_b = process_list_with_rules(list_b)
print(f"Final Result B: {result_b}")
# Expected: [10, 20, 40] (30 skipped, stops at 101)

print("-" * 30)

# Example 3: Edge case where the break condition is also a skip condition
list_c = [2, 4, 6, 102, 104]
result_c = process_list_with_rules(list_c)
print(f"Final Result C: {result_c}")
# Expected: [2, 4] (6 skipped, stops at 102 because the BREAK is checked first)