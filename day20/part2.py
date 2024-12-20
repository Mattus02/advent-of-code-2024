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

def InBounds(r, c):
    return r >= 0 and r < ROWS and c >= 0 and c < COLS

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
            if InBounds(nr, nc) and grid[nr][nc] != '#' and cost[nr][nc] > d + 1:
                stack.append((nr, nc, d + 1))
                cost[nr][nc] = d + 1
                
Search()

picos = 70

memory = set()

def Search2(R, C):
    result = 0
    for r in range(R-20, R+20):
        for c in range(C-20, C+20):
            if InBounds(r, c) and grid[r][c] != '#':
                manhattanDist = abs(R - r) + abs(C - c)
                if manhattanDist <= 20 and abs(cost[R][C] - cost[r][c]) >= picos + manhattanDist and ((R, C, r, c)) not in memory:
                    result += 1
                    memory.add((r, c, R, C))
    return result

answer = 0
for r in range(ROWS):
    for c in range(COLS):
        if grid[r][c] != '#':
            answer += Search2(r, c)

print(answer)