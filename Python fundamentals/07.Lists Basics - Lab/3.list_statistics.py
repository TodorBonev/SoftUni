input_count = int(input())

positive_digits_list = []
negative_digits_list = []

for input_counter in range(input_count):
    current_input = int(input())
    if current_input >= 0:
        positive_digits_list.append(current_input)
    else:
        negative_digits_list.append(current_input)

count_of_positive_digits = len(positive_digits_list)
sum_of_negative_digits = sum(negative_digits_list)

print(positive_digits_list)
print(negative_digits_list)
print(f"Count of positives: {count_of_positive_digits}")
print(f"Sum of negatives: {sum_of_negative_digits}")