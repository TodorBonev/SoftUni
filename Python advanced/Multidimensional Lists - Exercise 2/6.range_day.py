def is_valid_move(row, col, matrix):
    return 0 <= row < 5 and 0 <= col < 5 and matrix[row][col] == '.'


def is_valid_shot(row, col, matrix):
    return 0 <= row < 5 and 0 <= col < 5 and matrix[row][col] == 'x'


directions = {'up': (-1, 0), 'down': (1, 0), 'right': (0, 1), 'left': (0, -1)}

matrix = [input().split() for _ in range(5)]

player_pos = [(r, c) for r in range(5) for c in range(5) if matrix[r][c] == 'A'][0]
targets_count = sum(row.count('x') for row in matrix)

killed_targets = []
number_of_commands = int(input())

for _ in range(number_of_commands):
    command = input().split()
    direction = command[1]

    if command[0] == 'shoot':
        row, col = player_pos
        d_row, d_col = directions[direction]
        while 0 <= row < 5 and 0 <= col < 5:
            row += d_row
            col += d_col
            if is_valid_shot(row, col, matrix):
                matrix[row][col] = '.'
                targets_count -= 1
                killed_targets.append([row, col])
                break

        if targets_count == 0:
            print(f'Training completed! All {len(killed_targets)} targets hit.')
            break

    elif command[0] == 'move':
        steps = int(command[2])
        d_row, d_col = directions[direction]
        new_row = player_pos[0] + d_row * steps
        new_col = player_pos[1] + d_col * steps

        if is_valid_move(new_row, new_col, matrix):
            matrix[player_pos[0]][player_pos[1]] = '.'
            matrix[new_row][new_col] = 'A'
            player_pos = [new_row, new_col]

if targets_count > 0:
    print(f'Training not completed! {targets_count} targets left.')

for target in killed_targets:
    print(target)



