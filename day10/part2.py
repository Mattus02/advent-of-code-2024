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

def distinct(r, c, h):
    if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[-1]) or grid[r][c] == '.' or grid[r][c] != h:
        return 0
    if h == 9:
        return 1
    result = 0
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dr, dc in moves:
        R = r + dr
        C = c + dc
        result += distinct(R, C, h+1)
    return result

answer = 0
for r, c in trailheads:
    answer += distinct(r, c, 0)

print(answer)