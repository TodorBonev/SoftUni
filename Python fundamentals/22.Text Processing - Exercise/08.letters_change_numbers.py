text = input().split()
sum = 0

for word in text:
    char = word[0]
    location = ord(char)
    if location >= 65 and location <= 90:
        location -= 64
    else:
        location -= 96
    string_as_a_digit = float(word[1:-1])
    if char.isupper():
        string_as_a_digit /= location
    else:
        string_as_a_digit *= location
    char = word[-1]
    location = ord(char)
    if location >= 65 and location <= 90:
        location -= 64
    else:
        location -= 96
    if char.isupper():
        string_as_a_digit -= location
    else:
        string_as_a_digit += location
    sum += string_as_a_digit

print(f"{sum:.2f}")