"""
The 'calc' library contains the 'add2' function that takes 2 values and adds
them together. If either value is a string (or both of them are), 'add2' ensures
they are both strings, thereby resulting in a concatenated result.
NOTE: If a value submitted to the 'add2' function is a float, it must be done so
in quotes (i.e. as a string).
"""

def conv(value):
    """
    Convert the input value to an integer if possible, otherwise to a float,
    and if both fail, return it as a string.
    """
    if isinstance(value, (int, float, str)):  # Ensure value is a valid type
        try:
            return int(value)
        except ValueError:
            try:
                return float(value)
            except ValueError:
                return str(value)
    else:
        raise TypeError(f"Unsupported type: {type(value)}")  # Handle invalid types


def add2(arg1, arg2):
    """
    Adds two values together. If either value is a string, both are converted
    to strings before concatenation. Otherwise, they are added mathematically.
    """
    arg1conv = conv(arg1)
    arg2conv = conv(arg2)

    # If either argument is a string, convert both to strings for concatenation
    if isinstance(arg1conv, str) or isinstance(arg2conv, str):
        return str(arg1conv) + str(arg2conv)

    # Otherwise, return numerical sum
    return arg1conv + arg2conv