first_num = int(input())
second_num = int(input())
third_num = int(input())


def sum_numbers(a1, b1):
    result = a1 + b1
    return result


def subtract(the_sum, c1):
    result = the_sum - c1
    return result


def add_and_subtract(a, b, c):
    sum_is = sum_numbers(a, b)
    result = subtract(sum_is, c)
    return result


print(add_and_subtract(first_num, second_num, third_num))