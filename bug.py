def function_with_uncommon_error(a, b):
    if a == 0:
        return 0  # This will cause a ZeroDivisionError
    return b / a

result = function_with_uncommon_error(0, 10)
print(result)