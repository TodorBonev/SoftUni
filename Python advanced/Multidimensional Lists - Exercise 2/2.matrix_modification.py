def is_valid(row, col, size):
    return 0 <= row < size and 0 <= col < size

size = int(input())
matrix = [list(map(int, input().split())) for _ in range(size)]

while True:
    command = input()
    if command == "END":
        break

    parts = command.split()
    if len(parts) != 4:
        print("Invalid coordinates")
        continue

    action, row, col, value = parts[0], int(parts[1]), int(parts[2]), int(parts[3])

    if not is_valid(row, col, size):
        print("Invalid coordinates")
        continue

    if action == "Add":
        matrix[row][col] += value
    elif action == "Subtract":
        matrix[row][col] -= value
    else:
        print("Invalid coordinates")

for row in matrix:
    print(" ".join(map(str, row)))
