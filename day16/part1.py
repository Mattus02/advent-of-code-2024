from heapq import *

grid = []

sr, sc = None, None
er, ec = None, None

file = open("input.txt")
for line in file:
    grid.append([])
    for char in line.strip():
        if char == 'E':
            er = len(grid) - 1
            ec = len(grid[-1])
        elif char == 'S':
            sr = len(grid) - 1
            sc = len(grid[-1])
        grid[-1].append(char)

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def dijkstra():

    visited = set()
    pq = [(0, sr, sc, RIGHT)]

    while len(pq) > 0:

        d, r, c, dir = heappop(pq)
        if r == er and c == ec:
            return d

        if (r, c, dir) in visited:
            continue
        visited.add((r, c, dir))

        rl = (dir - 1) % 4
        rr = (dir + 1) % 4

        heappush(pq, (d + 1000, r, c, rl))
        heappush(pq, (d + 1000, r, c, rr))

        dr, dc = dirs[dir]
        if grid[r + dr][c + dc] != '#':
            heappush(pq, (d + 1, r + dr, c + dc, dir))


print(dijkstra())