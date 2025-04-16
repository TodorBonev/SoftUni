num_sequence = input()
sentence = input()

num_sequence = num_sequence.split()
sentence = list(sentence)
index_list = []
index = 0

for current_number in num_sequence:
    for current_digit in current_number:
        index += int(current_digit)
    index_list.append(index)
    index = 0

message = []

for new_index in index_list:
    while new_index >= len(sentence):
        new_index -= len(sentence)
    message.append(sentence[new_index])
    sentence.pop(new_index)

print("".join(message))