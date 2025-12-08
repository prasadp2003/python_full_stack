def multi_type_sort(data):
    return sorted(data, key=lambda x: (isinstance(x, str), x))
items = [3, "banana", 1.2, "apple", 10, 5.5, "cat"]

print(multi_type_sort(items))
def multi_type_sort_safe(data):
    cleaned = [x for x in data if isinstance(x, (int, float, str))]
    return sorted(cleaned, key=lambda x: (isinstance(x, str), x))
