num_of_inputs = int(input())

result = 0
for input_counter in range(num_of_inputs):
    char = input()
    result += ord(char)

print(f"The sum equals: {result}")