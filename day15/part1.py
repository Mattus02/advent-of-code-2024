grid = []
pr, pc = None, None

file = open("input1.txt")
while True:
    line = file.readline().strip()
    if not line:
        break
    grid.append([])
    for char in line:
        if char == '@':
            pr = len(grid) - 1
            pc = line.index('@')
        grid[-1].append(char)

commands = []
while True:
    line = file.readline().strip()
    if not line:
        break
    for char in line:
        commands.append(char)

def Move(r, c, dr, dc):
    nr = r + dr
    nc = c + dc
    if grid[nr][nc] == '.':
        grid[nr][nc] = grid[r][c]
        grid[r][c] = '.'
        return True
    elif grid[nr][nc] == '#':
        return False
    else:
        if Move(nr, nc, dr, dc):
            grid[nr][nc] = grid[r][c]
            grid[r][c] = '.'
            return True
        return False

m = {'^':(-1, 0), 'v':(1, 0), '<':(0, -1), '>':(0, 1)}

for command in commands:
    dr, dc = m[command]
    if Move(pr, pc, dr, dc):
        pr += dr
        pc += dc
    
for line in grid:
    print("".join(line))

answer = 0
for r in range(len(grid)):
    for c in range(len(grid[-1])):
        if grid[r][c] == 'O':
            answer += r*100 + c

print(answer)
