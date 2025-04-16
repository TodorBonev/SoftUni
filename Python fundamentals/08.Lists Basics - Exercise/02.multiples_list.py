factor = int(input())
multiplier = int(input())

result_list = []

for multiplier_counter in range(1, multiplier + 1):
    result = factor * multiplier_counter
    result_list.append(result)

result_list.sort()

print(result_list)