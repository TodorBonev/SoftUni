def func_executor(*functions):
    result = []
    for func, args in functions:
        func_name = func.__name__
        func_result = func(*args)
        result.append(f"{func_name} - {func_result}")
    return '\n'.join(result)

