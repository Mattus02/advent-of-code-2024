grid = []
sr, sc = None, None

file = open("input.txt")
for line in file:
    grid.append([])
    for char in line.strip():
        if char == 'S':
            sr = len(grid) - 1
            sc = len(grid[-1])
        grid[-1].append(char)

ROWS = len(grid)
COLS = len(grid[-1])

cost = [[99999999 for _ in range(len(grid[-1]))] for _ in range(len(grid))]

def Search():
    stack = []
    stack.append((sr, sc, 0))
    cost[sr][sc] = 0
    while len(stack) > 0:
        r, c, d = stack.pop()
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in moves:
            nr = r + dr
            nc = c + dc
            if nr >= 0 and nr < ROWS and nc >= 0 and nc < COLS and grid[nr][nc] != '#' and cost[nr][nc] > d + 1:
                stack.append((nr, nc, d + 1))
                cost[nr][nc] = d + 1
                
Search()

picos = 20

answer = 0
for r in range(ROWS):
    for c in range(COLS - 2):
        if grid[r][c] != '#' and grid[r][c+1] == '#' and grid[r][c+2] != '#' and abs(cost[r][c] - cost[r][c+2]) >= picos + 2:
            answer += 1

for r in range(ROWS - 2):
    for c in range(COLS):
        if grid[r][c] != '#' and grid[r+1][c] == '#' and grid[r+2][c] != '#' and abs(cost[r][c] - cost[r+2][c]) >= picos + 2:
            answer += 1

print(answer)