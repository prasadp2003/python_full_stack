def custom_max(data_list):
    # Handle the case of an empty list
    if not data_list:
        raise ValueError("custom_max() arg is an empty sequence")
    
    # Start by assuming the first element is the maximum
    max_value = data_list[0]
    
    # Iterate through the rest of the list
    for element in data_list[1:]:
        # If the current element is greater than our current max, update max_value
        if element > max_value:
            max_value = element
            
    return max_value

# Example Usage:
my_list = [45, 12, 89, 7, 55]
max_result = custom_max(my_list) 
# print(f"List: {my_list}, Custom Max: {max_result}") # Output: 89

def custom_min(data_list):
    # Handle the case of an empty list
    if not data_list:
        raise ValueError("custom_min() arg is an empty sequence")
        
    # Start by assuming the first element is the minimum
    min_value = data_list[0]
    
    # Iterate through the rest of the list
    for element in data_list[1:]:
        # If the current element is smaller than our current min, update min_value
        if element < min_value:
            min_value = element
            
    return min_value

# Example Usage:
my_list = [45, 12, 89, 7, 55]
min_result = custom_min(my_list) 
# print(f"List: {my_list}, Custom Min: {min_result}") # Output: 7

def custom_sum(data_list):
    # Start the total accumulator at 0
    total = 0
    
    # Iterate through every element in the list
    for element in data_list:
        # Add the current element to the running total
        total = total + element
        
    return total

# Example Usage:
my_list = [45, 12, 89, 7, 55]
sum_result = custom_sum(my_list) 
# print(f"List: {my_list}, Custom Sum: {sum_result}") # Output: 208