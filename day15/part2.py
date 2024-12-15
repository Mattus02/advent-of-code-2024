grid = []
pr, pc = None, None

file = open("input3.txt")
while True:
    line = file.readline().strip()
    if not line:
        break
    grid.append([])
    for char in line:
        if char == '@':
            pr = len(grid) - 1
            pc = len(grid[-1])
            grid[-1].append('@')
            grid[-1].append('.')
        elif char == 'O':
            grid[-1].append('[')
            grid[-1].append(']')
        else:
            grid[-1].append(char)
            grid[-1].append(char)

commands = []
while True:
    line = file.readline().strip()
    if not line:
        break
    for char in line:
        commands.append(char)

def CanMove(r, c, dr, dc):
    if dr == 0:
        nc = c + dc
        if grid[r][nc] == '#':
            return False
        elif grid[r][nc] == '.':
            return True
        else:
            return CanMove(r, nc, dr, dc)
    else:
        nr = r + dr
        if grid[nr][c] == '#':
            return False
        if grid[nr][c] == '.':
            return True
        if grid[nr][c] == '[':
            return CanMove(nr, c, dr, dc) and CanMove(nr, c+1, dr, dc)
        else:
            return CanMove(nr, c, dr, dc) and CanMove(nr, c-1, dr, dc)
    

def Move(r, c, dr, dc):
    if dr == 0:
        nc = c + dc
        if grid[r][nc] == '.':
            grid[r][nc] = grid[r][c]
            grid[r][c] = '.'
            return
        else:
            Move(r, nc, dr, dc)
            grid[r][nc] = grid[r][c]
            grid[r][c] = '.'
    else:
        nr = r + dr
        if grid[nr][c] == '.':
            grid[nr][c] = grid[r][c]
            grid[r][c] = '.'
            return
        elif grid[nr][c] == '[':
            Move(nr, c, dr, dc)
            Move(nr, c+1, dr, dc)
            grid[nr][c] = grid[r][c]
            grid[r][c] = '.'
        else:
            Move(nr, c, dr, dc)
            Move(nr, c-1, dr, dc)
            grid[nr][c] = grid[r][c]
            grid[r][c] = '.'   
       
m = {'^':(-1, 0), 'v':(1, 0), '<':(0, -1), '>':(0, 1)}

for command in commands:
    dr, dc = m[command]
    if CanMove(pr, pc, dr, dc):
        Move(pr, pc, dr, dc)
        pr += dr
        pc += dc

answer = 0
for r in range(len(grid)):
    for c in range(len(grid[-1])):
        if grid[r][c] == '[':
            answer += r*100 + c

for line in grid:
    print("".join(line))

print(answer)
