def naval_battle(n, field, attacks):

    grid = [list(map(int, row.split())) for row in field]
    
    destroyed_ships = 0
    for attack in attacks:
        row, col = map(int, attack.split('-'))
        
        if grid[row][col] > 0:
            grid[row][col] -= 1
            
            if grid[row][col] == 0:
                destroyed_ships += 1
    
    return destroyed_ships

n = int(input())

field = [input() for _ in range(n)]

attacks = input().split()

print(naval_battle(n, field, attacks))
