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

marked = set()
marked.add((sr, sc))
marked.add((er, ec))

def dijkstraForwardAndReverse():

    visited = dict()
    pq = [(0, sr, sc, RIGHT)]
    DIST = None

    while len(pq) > 0:

        d, r, c, dir = heappop(pq)
        if r == er and c == ec:
            DIST = d
            break

        if (r, c, dir) in visited:
            continue
        visited[(r, c, dir)] = d

        rl = (dir - 1) % 4
        rr = (dir + 1) % 4

        heappush(pq, (d + 1000, r, c, rl))
        heappush(pq, (d + 1000, r, c, rr))

        dr, dc = dirs[dir]
        if grid[r + dr][c + dc] != '#':
            heappush(pq, (d + 1, r + dr, c + dc, dir))

    visitedRev = dict()
    pq = []
    heappush(pq, (0, er, ec, LEFT))
    heappush(pq, (0, er, ec, DOWN))
    heappush(pq, (0, er, ec, RIGHT))
    heappush(pq, (0, er, ec, UP))

    while len(pq) > 0:

        d, r, c, dir = heappop(pq)
        if r == sr and c == sc:
            return d

        if (r, c, dir) in visitedRev:
            continue
        visitedRev[(r, c, dir)] = d

        if (r, c, (dir + 2) % 4) in visited:
            if visited[(r, c, (dir + 2) % 4)] + d == DIST:
                marked.add((r, c))

        rl = (dir - 1) % 4
        rr = (dir + 1) % 4

        heappush(pq, (d + 1000, r, c, rl))
        heappush(pq, (d + 1000, r, c, rr))

        dr, dc = dirs[dir]
        if grid[r + dr][c + dc] != '#':
            heappush(pq, (d + 1, r + dr, c + dc, dir))

dijkstraForwardAndReverse()
print(len(marked))