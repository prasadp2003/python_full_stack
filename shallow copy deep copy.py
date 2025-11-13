import copy

# --- 1. Setup: The Original Nested List ---
# This list contains two inner lists, making it a compound (nested) object.
original_list = [
    [10, 20],  # Nested list 1 (mutable)
    [30, 40]   # Nested list 2 (mutable)
]

print("--- Initial State ---")
print(f"Original List: {original_list}")
print("-" * 30)

# -----------------------------------------------------
# --- 2. Shallow Copy Demonstration (copy.copy()) ---
# -----------------------------------------------------

shallow_copy = copy.copy(original_list)

print("--- Shallow Copy: Initial Check ---")
print(f"Original List ID (outer): {id(original_list)}")
print(f"Shallow Copy ID (outer):  {id(shallow_copy)} (Different outer object)")
print(f"Original Inner List 1 ID: {id(original_list[0])}")
print(f"Shallow Copy Inner List 1 ID: {id(shallow_copy[0])} (Same inner object)")
print("-" * 30)

# ACTION: Modify a nested element in the shallow copy.
# We change the second element of the first inner list (20 -> 999).
print("ACTION: Changing shallow_copy[0][1] to 999...")
shallow_copy[0][1] = 999

# Observe the results:
print("\n--- Shallow Copy Results ---")
print(f"Original List:  {original_list}")
print(f"Shallow Copy:   {shallow_copy}")
print("\n* Result Explanation: The original list was also changed.")
print("* Rationale: Shallow copy copied the REFERENCE to the nested list, so modifying it through the copy affects the original.")
print("-" * 30)


# -----------------------------------------------------
# --- 3. Deep Copy Demonstration (copy.deepcopy()) ---
# -----------------------------------------------------

# Reset the original list to its initial state for the next test
original_list = [
    [10, 20],
    [30, 40]
]

deep_copy = copy.deepcopy(original_list)

print("--- Deep Copy: Initial Check ---")
print(f"Original List ID (outer): {id(original_list)}")
print(f"Deep Copy ID (outer):     {id(deep_copy)} (Different outer object)")
print(f"Original Inner List 1 ID: {id(original_list[0])}")
print(f"Deep Copy Inner List 1 ID: {id(deep_copy[0])} (DIFFERENT inner object)")
print("-" * 30)

# ACTION: Modify a nested element in the deep copy.
# We change the first element of the first inner list (10 -> 888).
print("ACTION: Changing deep_copy[0][0] to 888...")
deep_copy[0][0] = 888

# Observe the results:
print("\n--- Deep Copy Results ---")
print(f"Original List:  {original_list}")
print(f"Deep Copy:      {deep_copy}")
print("\n* Result Explanation: The original list remains completely unchanged.")
print("* Rationale: Deep copy copied the inner list RECURSIVELY, so modifying the copy has no impact on the original data structure.")