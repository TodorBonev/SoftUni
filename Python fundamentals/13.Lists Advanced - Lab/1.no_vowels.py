string = input()
result = [char for char in string if char.lower() not in ['a', 'o', 'u', 'e', 'i']]

print("".join(result))