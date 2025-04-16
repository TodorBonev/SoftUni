num = int(input())

for row in range(1, num + 1):
    print("*" * row)

for bottom_row in range(num - 1, 0, -1):
    print("*" * bottom_row)