WIDTH = 101
HEIGHT = 103

robots = []
with open("input.txt") as file:
    for line in file:
        p, v = line.strip().split()
        p = p[2:].split(',')
        p = (int(p[0]), int(p[1]))
        v = v[2:].split(',')
        v = (int(v[0]), int(v[1]))
        robots.append((p, v))

def hasNeighbour(x, y, unique):
    return (x-1, y) in unique or (x-1, y-1) in unique or (x-1, y+1) in unique or (x, y-1) in unique or (x, y+1) in unique or (x+1, y-1) in unique or (x+1, y) in unique or (x+1, y+1) in unique

iterations = 1
while True:
    unique = set()
    for i in range(len(robots)):
        p, v = robots[i]
        x = (p[0] + v[0]) % WIDTH
        y = (p[1] + v[1]) % HEIGHT
        robots[i] = ((x, y), v)
        unique.add((x, y))
    finished = True
    notHasNeighbourCount = 0
    for x, y in unique:
        if not hasNeighbour(x, y, unique):
            notHasNeighbourCount += 1
            if notHasNeighbourCount > 130:
                finished = False
                break
    if finished:
        break
    iterations += 1

print(iterations)