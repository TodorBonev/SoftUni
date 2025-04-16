numbers = input()

num_list = numbers.split()
inverted_list = []

for digit in num_list:
    digit_as_integer = int(digit)
    if digit_as_integer < 0:
        digit_as_integer = abs(digit_as_integer)
        inverted_list.append(digit_as_integer)
    else:
        digit_as_integer = digit_as_integer * -1
        inverted_list.append(digit_as_integer)
print(inverted_list)