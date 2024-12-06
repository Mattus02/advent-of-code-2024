


grid = []
guard = None
obstacles = set()

with open("input.txt") as file:
    for line in file:
        grid.append([])
        for ch in line.strip():
            if ch == '#':
                obstacles.add((len(grid) - 1, line.index(ch)))
                None
            elif ch == '^':
                guard = (len(grid) - 1, line.index(ch))
            grid[-1].append(ch)

print(grid)
print(guard)
print(obstacles)

