def find_alice_and_rabbit_holes(field):
    alice_position, rabbit_positions = (), []
    for row in range(size):
        for col in range(size):
            if field[row][col] == "A":
                alice_position = (row, col)
            elif field[row][col] == "R":
                rabbit_positions.append((row, col))
    return alice_position, rabbit_positions


def is_valid_position(row, col):
    return 0 <= row < size and 0 <= col < size


def get_tea_bags(field, row, col):
    return int(field[row][col]) if field[row][col].isdigit() else False


size = int(input())
field = [input().split() for _ in range(size)]

directions = {
    'up': (-1, 0),
    'down': (+1, 0),
    'left': (0, -1),
    'right': (0, +1)
}

tea_bag_count = 0
alice_position, rabbit_holes = find_alice_and_rabbit_holes(field)
field[alice_position[0]][alice_position[1]] = "*"

while tea_bag_count < 10:
    move_command = input()
    row_offset, col_offset = directions[move_command]
    new_position = (alice_position[0] + row_offset, alice_position[1] + col_offset)

    if not is_valid_position(new_position[0], new_position[1]) or new_position in rabbit_holes:
        if new_position in rabbit_holes:
            field[new_position[0]][new_position[1]] = "*"
        print(f"Alice didn't make it to the tea party.")
        break

    collected_tea_bags = get_tea_bags(field, new_position[0], new_position[1])

    if collected_tea_bags:
        tea_bag_count += collected_tea_bags

    alice_position = new_position
    field[alice_position[0]][alice_position[1]] = "*"

if tea_bag_count >= 10:
    print(f"She did it! She went to the party.")

for row in field:
    print(*row)


