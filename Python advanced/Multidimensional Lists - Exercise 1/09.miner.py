def find_miner_position(field):
    for r in range(len(field)):
        for c in range(len(field[r])):
            if field[r][c] == 's':
                return r, c

size = int(input())
commands = input().split()
field = [input().split() for _ in range(size)]

miner_row, miner_col = find_miner_position(field)
coal_count = sum(row.count('c') for row in field)

directions = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

for command in commands:
    new_row, new_col = miner_row + directions[command][0], miner_col + directions[command][1]

    if 0 <= new_row < size and 0 <= new_col < size: 
        miner_row, miner_col = new_row, new_col

        if field[miner_row][miner_col] == 'c': 
            coal_count -= 1
            field[miner_row][miner_col] = '*'

            if coal_count == 0:
                print(f"You collected all coal! ({miner_row}, {miner_col})")
                exit()

        elif field[miner_row][miner_col] == 'e':  
            print(f"Game over! ({miner_row}, {miner_col})")
            exit()

print(f"{coal_count} pieces of coal left. ({miner_row}, {miner_col})")
