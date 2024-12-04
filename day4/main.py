def createGrid(filename):
    grid = []
    with open(filename) as file:
        for line in file:
            grid.append([])
            for ch in line:
                if ch != '\n':
                    grid[-1].append(ch)
    return grid

def part1():
    grid = createGrid("input1.txt")

    ROWS = len(grid)
    COLS = len(grid[0])

    next = {"X":"M", "M":"A", "A":"S"}
    def find(r, c, ch, dr, dc):
        if r < 0 or c < 0 or r >= ROWS or c >= COLS:
            return False
        if grid[r][c] != ch:
            return False
        if ch == "S":
            return True
        r, c = r+dr, c+dc
        return find(r, c, next[ch], dr, dc)

    def count(r, c):
        result = 0
        # Find diagonal up left
        if find(r, c, "X", -1, -1):
            result += 1
        # Find diagonal up right
        if find(r, c, "X", -1, 1):
            result += 1
        # Find diagonal down left
        if find(r, c, "X", 1, -1):
            result += 1
        # Find diagonal down right
        if find(r, c, "X", 1, 1):
            result += 1
        # Find vertical up
        if find(r, c, "X", -1, 0):
            result += 1
        # Find vertical down
        if find(r, c, "X", 1, 0):
            result += 1
        # Find horizontal right
        if find(r, c, "X", 0, 1):
            result += 1
        # Find horizontal left
        if find(r, c, "X", 0, -1):
            result += 1
        return result

    result = 0
    for r in range(ROWS):
        for c in range(COLS):
            result += count(r, c)
    print(result)

def part2():
    grid = createGrid("input2.txt")

    ROWS = len(grid)
    COLS = len(grid[0])

    def findDiag1(r, c):
        if r == 0 or c == 0 or r == ROWS-1 or c == COLS-1:
            return False
        return (grid[r-1][c-1] == "M" and grid[r+1][c+1] == "S") or (grid[r-1][c-1] == "S" and grid[r+1][c+1] == "M")

    def findDiag2(r, c):
        if r == 0 or c == 0 or r == ROWS-1 or c == COLS-1:
            return False
        return (grid[r+1][c-1] == "M" and grid[r-1][c+1] == "S") or (grid[r+1][c-1] == "S" and grid[r-1][c+1] == "M")

    def find(r, c):
        return findDiag1(r, c) and findDiag2(r, c)

    result = 0
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == "A":
                result += find(r, c)
    print(result)

part1()
part2()