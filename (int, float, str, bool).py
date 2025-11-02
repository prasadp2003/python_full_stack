def count_data_types(data_list):
    type_count = {'int': 0, 'float': 0, 'str': 0, 'bool': 0}
    
    for item in data_list:
        if isinstance(item, bool):
            type_count['bool'] += 1
        elif isinstance(item, int):
            type_count['int'] += 1
        elif isinstance(item, float):
            type_count['float'] += 1
        elif isinstance(item, str):
            type_count['str'] += 1
    
    return type_count


# Example usage:
data = [1, 2.5, "hello", True, False, 42, "world", 3.14]
result = count_data_types(data)
print(result)
