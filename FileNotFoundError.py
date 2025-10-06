def safe_file_reader(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return None


# Example usage:
data = safe_file_reader("example.txt")
if data:
    print("File contents:\n", data)
