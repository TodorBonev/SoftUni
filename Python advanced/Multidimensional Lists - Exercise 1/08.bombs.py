def is_valid_position(r, c, size):
    return 0 <= r < size and 0 <= c < size

def detonate_bomb(matrix, row, col, size):
    bomb_value = matrix[row][col]
    if bomb_value <= 0:
        return
    matrix[row][col] = 0 

    directions = [(-1, -1), (-1, 0), (-1, 1), 
                  (0, -1), (0, 1),
                  (1, -1), (1, 0), (1, 1)]
    
    for dr, dc in directions:
        new_r, new_c = row + dr, col + dc
        if is_valid_position(new_r, new_c, size) and matrix[new_r][new_c] > 0:
            matrix[new_r][new_c] -= bomb_value

size = int(input())
matrix = [list(map(int, input().split())) for _ in range(size)]
bombs = [tuple(map(int, bomb.split(","))) for bomb in input().split()]

for bomb in bombs:
    detonate_bomb(matrix, bomb[0], bomb[1], size)

alive_cells = sum(1 for row in matrix for value in row if value > 0)
sum_alive_cells = sum(value for row in matrix for value in row if value > 0)

print(f"Alive cells: {alive_cells}")
print(f"Sum: {sum_alive_cells}")
for row in matrix:
    print(" ".join(map(str, row)))
