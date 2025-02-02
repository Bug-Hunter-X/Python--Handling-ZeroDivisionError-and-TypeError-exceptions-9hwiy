def function_with_uncommon_error(x, y):
    try:
        result = x / y
        return result
    except ZeroDivisionError:
        return float('inf')
    except TypeError:
        return 'Error: Invalid input types'

# Example usage
print(function_with_uncommon_error(10, 2))  # Output: 5.0
print(function_with_uncommon_error(10, 0))  # Output: inf
print(function_with_uncommon_error(10, 'a')) # Output: Error: Invalid input types
print(function_with_uncommon_error(10, [])) # Output: Error: Invalid input types