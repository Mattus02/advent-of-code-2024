grid = []

with open("input.txt") as file:
    for line in file:
        grid.append([])
        for ch in line:
            if ch != '\n':
                grid[-1].append(ch)

ROWS = len(grid)
COLS = len(grid[0])

visited = [[False for _ in range(COLS)] for _ in range(ROWS)]

def hasEdgeUp(r, c):
    return r == 0 or grid[r-1][c] != grid[r][c]

def checkEdgeUp(r, c, dc, symbol, regUp):
    if c >= 0 and c < COLS and hasEdgeUp(r, c) and grid[r][c] == symbol:
        regUp.add((r, c))
        checkEdgeUp(r, c + dc, dc, symbol, regUp)

def hasEdgeDown(r, c):
    return r == ROWS - 1 or grid[r+1][c] != grid[r][c]

def checkEdgeDown(r, c, dc, symbol, regDown):
    if c >= 0 and c < COLS and hasEdgeDown(r, c) and grid[r][c] == symbol:
        regDown.add((r, c))
        checkEdgeDown(r, c + dc, dc, symbol, regDown)

def hasEdgeLeft(r, c):
    return c == 0 or grid[r][c-1] != grid[r][c]

def checkEdgeLeft(r, c, dr, symbol, regLeft):
    if r >= 0 and r < ROWS and hasEdgeLeft(r, c) and grid[r][c] == symbol:
        regLeft.add((r, c))
        checkEdgeLeft(r + dr, c, dr, symbol, regLeft)

def hasEdgeRight(r, c):
    return c == COLS - 1 or grid[r][c+1] != grid[r][c]

def checkEdgeRight(r, c, dr, symbol, regRight):
    if r >= 0 and r < ROWS and hasEdgeRight(r, c) and grid[r][c] == symbol:
        regRight.add((r, c))
        checkEdgeRight(r + dr, c, dr, symbol, regRight)


def dontEvenKnowWhatToNameThis(r, c):
    symbol = grid[r][c]
    area = 0
    sides = 0
    stack = [(r, c)]
    visited[r][c] = True
    regUp = set()
    regDown = set()
    regLeft = set()
    regRight = set()
    while len(stack) > 0:
        r, c = stack.pop()
        area += 1
        if hasEdgeUp(r, c) and (r, c) not in regUp:
            checkEdgeUp(r, c-1, -1, symbol, regUp)
            checkEdgeUp(r, c+1, +1, symbol, regUp)
            sides += 1
        if hasEdgeDown(r, c) and (r, c) not in regDown:
            checkEdgeDown(r, c-1, -1, symbol, regDown)
            checkEdgeDown(r, c+1, +1, symbol, regDown)
            sides += 1
        if hasEdgeLeft(r, c) and (r, c) not in regLeft:
            checkEdgeLeft(r-1, c, -1, symbol, regLeft)
            checkEdgeLeft(r+1, c, +1, symbol, regLeft)
            sides += 1
        if hasEdgeRight(r, c) and (r, c) not in regRight:
            checkEdgeRight(r-1, c, -1, symbol, regRight)
            checkEdgeRight(r+1, c, +1, symbol, regRight)
            sides += 1
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in moves:
            R = r + dr
            C = c + dc
            if R < 0 or R >= ROWS or C < 0 or C >= COLS:
                continue
            if grid[R][C] == symbol and not visited[R][C]:
                stack.append((R, C))
                visited[R][C] = True
    return area * sides
        

answer = 0
for r in range(ROWS):
    for c in range(COLS):
        if not visited[r][c]:
            answer += dontEvenKnowWhatToNameThis(r, c)

print(answer)