num_input = input()


def odd_and_even_sum(num_string):
    odd_sum = 0
    even_sum = 0
    for num in num_string:
        if int(num) % 2 == 0:
            even_sum += int(num)
        else:
            odd_sum += int(num)
    output = f"Odd sum = {odd_sum}, Even sum = {even_sum}"
    return output


print(odd_and_even_sum(num_input))