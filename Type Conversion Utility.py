def convert_types(data_dict):
    """
    Converts string values in a dictionary to their most likely Python types.
    Supported types: int, float, bool, str
    """
    converted = {}

    for key, value in data_dict.items():
        val = value.strip().lower()

        # Check for boolean
        if val == "true":
            converted[key] = True
        elif val == "false":
            converted[key] = False
        else:
            # Try integer conversion
            try:
                converted[key] = int(value)
            except ValueError:
                # Try float conversion
                try:
                    converted[key] = float(value)
                except ValueError:
                    # Keep as string
                    converted[key] = value
    return converted


# Example usage:
data = {
    "age": "25",
    "height": "5.9",
    "is_student": "True",
    "name": "Alice",
    "score": "89.5",
    "has_passed": "false"
}

converted_data = convert_types(data)

