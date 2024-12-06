# Not pretty and not optimized code, sorry :)

# Common start

grid = []
startPosition = None
obstacles = set()

with open("input.txt") as file:
    for line in file:
        grid.append([])
        for ch in line.strip():
            if ch == '#':
                obstacles.add((len(grid) - 1, len(grid[-1])))
                None
            elif ch == '^':
                startPosition = (len(grid) - 1, len(grid[-1]))
            grid[-1].append(ch)

nextDirection = {(-1, 0):(0, 1), (0, 1):(1, 0), (1, 0):(0, -1), (0, -1):(-1, 0)}

position = startPosition
direction = (-1, 0)
distinctPositions = set()

def OutOfBounds(position):
    r, c = position
    return r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0])

def walk(position, direction):
    if position not in distinctPositions:
        distinctPositions.add(position)
    r, c = position
    dr, dc = direction
    nr, nc = r + dr, c + dc
    if (nr, nc) in obstacles:
        return (r, c), nextDirection[direction]
    return (nr, nc), direction

while not OutOfBounds(position):
    position, direction = walk(position, direction)

print(len(distinctPositions)) # Answer for part 1

# Part 2

distinctPositions.remove(startPosition)

def walk2(position, direction, distinctPositionsTmp):
    distinctPositionsTmp.add((position, direction))
    r, c = position
    dr, dc = direction
    nr, nc = r + dr, c + dc
    if (nr, nc) in obstacles:
        return (r, c), nextDirection[direction]
    return (nr, nc), direction

def isLoop(position, direction):
    distinctPositionsTmp = set()
    while not OutOfBounds(position):
        if (position, direction) in distinctPositionsTmp:
            return 1
        position, direction = walk2(position, direction, distinctPositionsTmp)
    return 0

result = 0
for pos in distinctPositions:
    obstacles.add(pos)
    result += isLoop(startPosition, (-1, 0))
    obstacles.remove(pos)

print(result) # Answer for part 2