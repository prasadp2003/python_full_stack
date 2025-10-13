import time

# Decorator definition
def log_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()           # Record start time
        result = func(*args, **kwargs)     # Execute the original function
        end_time = time.time()             # Record end time
        execution_time = end_time - start_time
        print(f"Function '{func.__name__}' executed in {execution_time:.4f} seconds.")
        return result
    return wrapper

# Example usage
@log_execution_time
def slow_function():
    time.sleep(2)
    print("Finished slow function.")

@log_execution_time
def add(a, b):
    time.sleep(1)
    return a + b

# Test the decorator
slow_function()
print(add(5, 10))
