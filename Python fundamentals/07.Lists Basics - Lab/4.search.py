input_count = int(input())
special_word = input()

list_of_words = []

for input_counter in range(input_count):
    current_input = input()
    list_of_words.append(current_input)

filtered_list_of_words = []

for index in range(len(list_of_words)):
    if special_word in list_of_words[index]:
        filtered_list_of_words.append(list_of_words[index])

print(list_of_words)
print(filtered_list_of_words)