count_of_inputs = int(input())

numbers_list = []

for input_counter in range(count_of_inputs):
    current_num = int(input())
    numbers_list.append(current_num)
command = input()

filtered_numbers_list = []

for index in range(len(numbers_list)):
    if command == "even":
        if numbers_list[index] % 2 == 0:
            filtered_numbers_list.append(numbers_list[index])
    elif command == "odd":
        if numbers_list[index] % 2 != 0:
            filtered_numbers_list.append(numbers_list[index])
    elif command == "negative":
        if numbers_list[index] < 0:
            filtered_numbers_list.append(numbers_list[index])
    elif command == "positive":
        if numbers_list[index] >= 0:
            filtered_numbers_list.append(numbers_list[index])

print(filtered_numbers_list)