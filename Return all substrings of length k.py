def substrings_of_length_k(s, k):
    # Handle edge cases
    if k <= 0 or k > len(s):
        return []

    substrings = []
    for i in range(len(s) - k + 1):
        substrings.append(s[i:i+k])
    return substrings

# Example usage
string = "abcdef"
k = 3
result = substrings_of_length_k(string, k)
print(result)
