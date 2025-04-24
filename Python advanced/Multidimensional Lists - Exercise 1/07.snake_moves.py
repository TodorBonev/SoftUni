rows, cols = map(int, input().split())
snake = input()

matrix = [['' for _ in range(cols)] for _ in range(rows)]
index = 0

for r in range(rows):
    if r % 2 == 0:
        for c in range(cols):
            matrix[r][c] = snake[index % len(snake)]
            index += 1
    else:
        for c in range(cols - 1, -1, -1):
            matrix[r][c] = snake[index % len(snake)]
            index += 1

for row in matrix:
    print("".join(row))
