def is_valid(coords, rows, cols):
    return all(0 <= coords[i] < (rows if i % 2 == 0 else cols) for i in range(4))

rows, cols = map(int, input().split())
matrix = [input().split() for _ in range(rows)]

while True:
    command = input()
    if command == "END":
        break
    
    parts = command.split()
    if parts[0] != "swap" or len(parts) != 5:
        print("Invalid input!")
        continue

    row1, col1, row2, col2 = map(int, parts[1:])
    
    if not is_valid([row1, col1, row2, col2], rows, cols):
        print("Invalid input!")
        continue

    matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
    
    for row in matrix:
        print(" ".join(row))
