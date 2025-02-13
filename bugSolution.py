def function_with_uncommon_error(a, b):
    if a == 0:
        return 0 #This is to handle the case when a is 0
    try:
        result = b / a
        return result
    except ZeroDivisionError:
        return "Division by Zero"

result = function_with_uncommon_error(0, 10)
print(result)