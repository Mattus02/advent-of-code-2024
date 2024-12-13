

grid = []

with open("input2.txt") as file:
    for line in file:
        grid.append([])
        for ch in line:
            if ch != '\n':
                grid[-1].append(ch)

ROWS = len(grid)
COLS = len(grid[0])

visited = [[False for _ in range(COLS)] for _ in range(ROWS)]

def DFS(r, c):
    symbol = grid[r][c]
    area = 0
    peri = 0
    stack = [(r, c)]
    visited[r][c] = True
    while len(stack) > 0:
        r, c = stack.pop()
        area += 1
        if r == 0 or r == ROWS-1:
            peri += 1
        if c == 0 or c == COLS-1:
            peri += 1
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in moves:
            R = r + dr
            C = c + dc
            if R < 0 or R >= ROWS or C < 0 or C >= COLS:
                continue
            if grid[R][C] == symbol:
                if not visited[R][C]:
                    stack.append((R, C))
                    visited[R][C] = True
            else:
                peri += 1
    return area * peri
        

answer = 0
for r in range(ROWS):
    for c in range(COLS):
        if not visited[r][c]:
            answer += DFS(r, c)

print(answer)