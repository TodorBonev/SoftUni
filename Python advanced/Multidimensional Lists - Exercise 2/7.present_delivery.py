def move_santa(row, col, direction):
    directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
    return row + directions[direction][0], col + directions[direction][1]


def is_within_bounds(row, col, size):
    return 0 <= row < size and 0 <= col < size


def get_adjacent_kids(matrix, row, col):
    kids_positions = []
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        new_row, new_col = row + dr, col + dc
        if is_within_bounds(new_row, new_col, len(matrix)) and matrix[new_row][new_col] in ('X', 'V'):
            kids_positions.append([new_row, new_col])
    return kids_positions


gifts = int(input())
size = int(input())

matrix = []
santa_row = santa_col = nice_kids = 0

for row in range(size):
    row_elements = input().split()
    for col in range(size):
        if row_elements[col] == 'S':
            santa_row, santa_col = row, col
        elif row_elements[col] == 'V':
            nice_kids += 1
    matrix.append(row_elements)

gifted_kids = 0

while gifts > 0:
    command = input()
    if command == 'Christmas morning':
        break

    matrix[santa_row][santa_col] = '-'
    santa_row, santa_col = move_santa(santa_row, santa_col, command)

    if matrix[santa_row][santa_col] == 'V':
        gifts -= 1
        gifted_kids += 1
    elif matrix[santa_row][santa_col] == 'C':
        adjacent_kids = get_adjacent_kids(matrix, santa_row, santa_col)
        for kid_row, kid_col in adjacent_kids:
            if matrix[kid_row][kid_col] == 'V':
                gifted_kids += 1
            gifts -= 1
            matrix[kid_row][kid_col] = '-'
            if gifts == 0:
                break

    matrix[santa_row][santa_col] = 'S'

if gifted_kids != nice_kids and gifts == 0:
    print("Santa ran out of presents!")

for row in matrix:
    print(*row)

if gifted_kids == nice_kids:
    print(f"Good job, Santa! {nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids - gifted_kids} nice kid/s.")

