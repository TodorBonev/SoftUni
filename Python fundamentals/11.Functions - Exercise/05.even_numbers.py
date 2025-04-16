integers_as_string = input()

integers_list = [int(char) for char in integers_as_string.split()]


def even_nums(current_num):
    if current_num % 2 == 0:
        return True
    else:
        return False

is_it_even = filter(even_nums, integers_list)
even_numbers_list = []

for current_even_num in is_it_even:
    even_numbers_list.append(current_even_num)
print(even_numbers_list)