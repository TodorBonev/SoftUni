num_of_inputs = int(input())

is_it_balanced = False
left_bracket_counter = 0
right_bracket_counter = 0

for input_counter in range(num_of_inputs):
    concurrent_input = input()
    if concurrent_input == "(":
        left_bracket_counter += 1
    if left_bracket_counter == 1 and concurrent_input == ")":
        left_bracket_counter = 0
        is_it_balanced = True
    elif left_bracket_counter == 0 and concurrent_input == ")":
        is_it_balanced = False
        break

if is_it_balanced:
    print("BALANCED")
else:
    print("UNBALANCED")