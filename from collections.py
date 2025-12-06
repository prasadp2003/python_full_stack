from collections.abc import Mapping, Sequence
from numbers import Number

def sum_nested(data):
    """
    Recursively traverse a nested structure of dicts/lists/tuples/etc.
    and sum all numeric (int/float) values.
    Non-numeric values are ignored.
    """
    total = 0

    # If it's a dict / mapping → traverse its values
    if isinstance(data, Mapping):
        for value in data.values():
            total += sum_nested(value)

    # If it's a list/tuple/etc (but not string/bytes)
    elif isinstance(data, Sequence) and not isinstance(data, (str, bytes, bytearray)):
        for item in data:
            total += sum_nested(item)

    # If it's a number → add it (but avoid treating bool as number)
    elif isinstance(data, Number) and not isinstance(data, bool):
        total += data

    # Everything else is ignored (str, None, objects, etc.)
    return total
