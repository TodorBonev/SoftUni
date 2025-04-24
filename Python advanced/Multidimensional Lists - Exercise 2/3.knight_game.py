def get_attacking_knights(board, size):
    moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
             (1, -2), (1, 2), (2, -1), (2, 1)]
    
    attacking_knights = []
    
    for r in range(size):
        for c in range(size):
            if board[r][c] == "K":
                attack_count = sum(
                    1 for dr, dc in moves 
                    if 0 <= r + dr < size and 0 <= c + dc < size and board[r + dr][c + dc] == "K"
                )
                if attack_count:
                    attacking_knights.append((attack_count, r, c))

    return attacking_knights

def remove_knights(board, size):
    removed_knights = 0

    while True:
        attacking_knights = get_attacking_knights(board, size)
        
        if not attacking_knights:
            break
        
        attacking_knights.sort(reverse=True, key=lambda x: (x[0], -x[1], -x[2]))
        _, row, col = attacking_knights[0]
        board[row][col] = "0"
        removed_knights += 1

    return removed_knights

size = int(input())
board = [list(input()) for _ in range(size)]

print(remove_knights(board, size))
