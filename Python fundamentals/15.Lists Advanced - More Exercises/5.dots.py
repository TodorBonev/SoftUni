def dfs(board, r, c, visited):
    if (r < 0 or r >= len(board) or c < 0 or c >= len(board[0]) or 
        board[r][c] != '.' or (r, c) in visited):
        return 0

    visited.add((r, c))
    size = 1
    
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        size += dfs(board, r + dr, c + dc, visited)
    
    return size

n = int(input())
board = [input().split() for _ in range(n)]

visited = set()
max_cluster = 0

for r in range(n):
    for c in range(len(board[0])):
        if board[r][c] == '.' and (r, c) not in visited:
            max_cluster = max(max_cluster, dfs(board, r, c, visited))

print(max_cluster)
