names = input().split(", ")
valid_names = []

for name in names:
    isValid = True
    if not 3 < len(name) < 16:
        continue
    for char in name:
        if not char.isdigit() and not char.isalpha() and not char == "-" and not char == "_":
            isValid = False
        if " " in char:
            isValid = False
    if isValid:
        valid_names.append(name)

for name in valid_names:
    print(name)