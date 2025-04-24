def find_player(matrix):
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] == 'P':
                return r, c
    return None

def spread_bunnies(matrix):
    new_bunnies = set()
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] == 'B':
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < len(matrix) and 0 <= nc < len(matrix[0]):
                        new_bunnies.add((nr, nc))
    
    for r, c in new_bunnies:
        matrix[r][c] = 'B'

def play_game(rows, cols, matrix, commands):
    player_pos = find_player(matrix)
    directions = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}

    for command in commands:
        r, c = player_pos
        nr, nc = r + directions[command][0], c + directions[command][1]

        if 0 <= nr < rows and 0 <= nc < cols: 
            if matrix[nr][nc] == 'B':
                spread_bunnies(matrix)
                print_game(matrix)
                print(f"dead: {nr} {nc}")
                return
            matrix[r][c] = "." 
            player_pos = (nr, nc)
        else: 
            matrix[r][c] = "."  
            spread_bunnies(matrix)
            print_game(matrix)
            print(f"won: {r} {c}")
            return

        spread_bunnies(matrix)
        if matrix[player_pos[0]][player_pos[1]] == 'B':
            print_game(matrix)
            print(f"dead: {player_pos[0]} {player_pos[1]}")
            return

    print_game(matrix)
    print(f"dead: {player_pos[0]} {player_pos[1]}")

def print_game(matrix):
    for row in matrix:
        print("".join(row))

rows, cols = map(int, input().split())
matrix = [list(input()) for _ in range(rows)]
commands = input()

play_game(rows, cols, matrix, commands)

