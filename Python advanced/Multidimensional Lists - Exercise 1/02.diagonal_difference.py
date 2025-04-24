size = int(input())
matrix = [list(map(int, input().split())) for _ in range(size)]

primary_sum = sum(matrix[i][i] for i in range(size))
secondary_sum = sum(matrix[i][size - i - 1] for i in range(size))

print(abs(primary_sum - secondary_sum))
