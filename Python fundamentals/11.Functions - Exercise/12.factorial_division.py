number1_input = int(input())
number2_input = int(input())

def factorial_division(num):
    if num == 0:
        result = 1
        return result
    else:
        result = num
        for factor in range(num - 1, 0, -1):
            result *= factor
        return result

outcome = factorial_division(number1_input) / factorial_division(number2_input)

print(f"{outcome:.2f}")