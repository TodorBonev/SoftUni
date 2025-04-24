rows, cols = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(rows)]

max_sum, best_square = float('-inf'), []

for r in range(rows - 2):
    for c in range(cols - 2):
        square = [matrix[i][c:c+3] for i in range(r, r+3)]
        square_sum = sum(sum(row) for row in square)

        if square_sum > max_sum:
            max_sum, best_square = square_sum, square

print(f"Sum = {max_sum}")
for row in best_square:
    print(*row)
