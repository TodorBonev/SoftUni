text = input()
new_text = ""
counter = 0

for char in text:
    if char == ">":
        new_text += char
        continue
    elif char.isdigit():
        counter += int(char)
    if counter > 0:
        counter -= 1
        continue
    else:
        new_text += char
    if counter < 0:
        counter = 0

print(new_text)