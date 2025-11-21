def custom_formatter(template: str, data: dict) -> str:
    """
    Replaces placeholders in a template string with values from a dictionary.

    Placeholders should be in the format {key}.
    If a key is missing in the dictionary, the original placeholder is left in the string.

    Args:
        template: The string containing placeholders.
        data: The dictionary containing the values for replacement.

    Returns:
        The formatted string.
    """
    import re
    
    # The regex pattern finds strings that start with '{' and end with '}'
    # The '?' makes the matching non-greedy, so it stops at the first '}'.
    pattern = r'{(.*?)}'
    
    def replacer(match):
        # match.group(0) is the full match, e.g., "{name}"
        # match.group(1) is the content inside the braces, e.g., "name"
        key = match.group(1)
        
        # Look up the key in the dictionary
        # .get() is used for graceful handling of missing keys:
        # If the key is present, it returns the value (which is converted to a string).
        # If the key is missing, it returns the default value, which is the original 
        # placeholder string (e.g., "{key}")
        
        return str(data.get(key, match.group(0)))

    # Use re.sub() to apply the replacer function to every match of the pattern
    # The replacer function handles the lookup and missing key scenario for each match.
    return re.sub(pattern, replacer, template)
# 1. Define the template string with placeholders
template_str = "Hello, {name}! Your age is {age} and your city is {city}. The job title is {job_title}."

# 2. Define the data dictionary (notice 'city' and 'job_title' are missing)
data_dict = {
    "name": "Alex",
    "age": 30
    # 'city' and 'job_title' are missing keys
}

# 3. Call the function
formatted_result = custom_formatter(template_str, data_dict)

# 4. Print the result
print(formatted_result)