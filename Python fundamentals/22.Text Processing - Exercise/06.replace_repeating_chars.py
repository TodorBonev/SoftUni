text = input()
filtered_letters = []
current_letter = ""

for letter in text:
    if letter != current_letter:
        current_letter = letter
        filtered_letters.append(letter)
print(''.join(filtered_letters))