input_operator = input()
input_a = int(input())
input_b = int(input())


def calculator(operator, a, b):
    result = 0
    if operator == "multiply":
        result = a * b
    elif operator == "divide":
        result = a // b
    elif operator == "add":
        result = a + b
    elif operator == "subtract":
        result = a - b
    return result


print(calculator(input_operator, input_a, input_b))