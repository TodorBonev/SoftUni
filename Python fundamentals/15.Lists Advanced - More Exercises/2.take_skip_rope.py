text = input()

numbers = [int(ch) for ch in text if ch.isdigit()]
non_numbers = [ch for ch in text if not ch.isdigit()]

take_list = numbers[::2]
skip_list = numbers[1::2]

result = []
index = 0

for take, skip in zip(take_list, skip_list):
    result.extend(non_numbers[index:index+take])
    index += take + skip

print("".join(result))
