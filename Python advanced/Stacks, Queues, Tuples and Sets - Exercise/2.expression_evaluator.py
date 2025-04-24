from collections import deque
import math

def evaluate_expression(expression):
    tokens = deque(expression.split())
    numbers = deque()

    while tokens:
        token = tokens.popleft()
        if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
            numbers.append(int(token))
        else:
            result = numbers.popleft()
            while numbers:
                num = numbers.popleft()
                if token == "+":
                    result += num
                elif token == "-":
                    result -= num
                elif token == "*":
                    result *= num
                elif token == "/":
                    result = math.floor(result / num) 
            numbers.append(result)

    print(numbers[0])

expression = input()
evaluate_expression(expression)
