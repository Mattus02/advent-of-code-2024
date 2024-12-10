grid = []
trailheads = set()

file = open("input.txt")
for line in file:
    grid.append([])
    for char in line.strip():
        if char.isdigit():
            digit = int(char)
            if digit == 0:
                trailheads.add((len(grid) - 1, len(grid[-1])))
            grid[-1].append(digit)
        else:
            grid[-1].append('.')

def DFS(r, c):
    found9s = set()
    stack = []
    stack.append((r, c, 0))
    while len(stack) > 0:
        r, c, h = stack.pop()
        if h == 9:
            found9s.add((r, c))
        else:
            moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dr, dc in moves:
                R = r + dr
                C = c + dc
                if R >= 0 and R < len(grid) and C >= 0 and C < len(grid[-1]) and grid[R][C] != '.' and grid[R][C] == h + 1:
                    stack.append((R, C, h+1))
    return len(found9s)

answer = 0
for r, c in trailheads:
    answer += DFS(r, c)

print(answer)