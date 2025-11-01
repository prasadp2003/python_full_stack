def dynamic_input_parser(user_input):
    """
    Parses a line of input into appropriate Python data types:
    int, float, bool, or str.

    Args:
        user_input (str): Input string from the user.

    Returns:
        list: List of parsed values with correct data types.
    """
    def parse_value(value):
        # Try to convert to int
        try:
            return int(value)
        except ValueError:
            pass

        # Try to convert to float
        try:
            return float(value)
        except ValueError:
            pass

        # Convert to boolean if possible
        val_lower = value.lower()
        if val_lower in ('true', 'false'):
            return val_lower == 'true'

        # Otherwise, return as string
        return value

    # Split input by spaces and parse each token
    parts = user_input.split()
    return [parse_value(part) for part in parts]


# Example usage:
if __name__ == "__main__":
    line = input("Enter values separated by spaces: ")
    parsed_values = dynamic_input_parser(line)
    print("Parsed Output:", parsed_values)
