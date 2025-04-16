n = int(input())
maze = [list(input()) for _ in range(n)]

k_idx = next(([i, row.index("k")] for i, row in enumerate(maze) if "k" in row), None)
maze[k_idx[0]][k_idx[1]] = " "

visited, steps, steps_old, flag = [k_idx], 0, -1, False
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def find_spaces(k, ma):
    return [[k[0] + dr, k[1] + dc] for dr, dc in directions if 0 <= k[0] + dr < len(ma) and 0 <= k[1] + dc < len(ma[0]) and ma[k[0] + dr][k[1] + dc] == " "]

def move(k, s, v, maze, m):
    for space in s:
        if space not in v:
            v.append(space)
            return space, v, m + 1
    maze[k[0]][k[1]] = "@"
    return v[-2], v[:-1], m - 1

while k_idx[0] < n:
    if k_idx[0] in {0, n - 1} or k_idx[1] in {0, len(maze[0]) - 1}: 
        steps_old = max(steps, steps_old)

    spaces = find_spaces(k_idx, maze)  
    if not spaces and steps_old == -1:
        print("Kate cannot get out")
        flag = True
        break
    elif not spaces and steps_old != -1:
        steps = steps_old
        break

    k_idx, visited, steps = move(k_idx, spaces, visited, maze, steps)

if not flag:
    print(f"Kate got out in {steps + 1} moves")



