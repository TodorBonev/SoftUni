rows, cols = map(int, input().split())
matrix = [input().split() for _ in range(rows)]
count = sum(
    1 for r in range(rows - 1) for c in range(cols - 1)
    if matrix[r][c] == matrix[r][c + 1] == matrix[r + 1][c] == matrix[r + 1][c + 1]
)

print(count)
