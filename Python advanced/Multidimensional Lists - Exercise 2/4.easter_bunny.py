size = int(input())
field = [input().split() for _ in range(size)]
bunny_x, bunny_y = next((x, row.index('B')) for x, row in enumerate(field) if 'B' in row)

directions = {
    'right': lambda x, y: (x, y + 1),
    'left': lambda x, y: (x, y - 1),
    'up': lambda x, y: (x - 1, y),
    'down': lambda x, y: (x + 1, y)
}

max_eggs, best_direction, best_route = float('-inf'), '', []

for direction, move in directions.items():
    eggs, path = 0, []
    x, y = move(bunny_x, bunny_y)
    while 0 <= x < size and 0 <= y < size and field[x][y] != 'X':
        eggs += int(field[x][y])
        path.append([x, y])
        x, y = move(x, y)
    if eggs > max_eggs:
        max_eggs, best_direction, best_route = eggs, direction, path

print(best_direction)
print(*best_route, sep='\n')
print(max_eggs)








