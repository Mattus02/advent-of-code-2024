from heapq import *

occupied = [[False for _ in range(71)] for _ in range(71)]


file = open("input.txt")
for _ in range(1024):
    x, y = map(int, file.readline().strip().split(','))
    occupied[x][y] = True


def dijkstra():
    visited = [[False for _ in range(71)] for _ in range(71)]
    pq = [(0, 0, 0)]
    while len(pq) > 0:

        d, x, y = heappop(pq)

        if visited[x][y]:
            continue
        visited[x][y] = True

        if x == 70 and y == 70:
            return d

        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if nx >= 0 and nx < 71 and ny >= 0 and ny < 71 and not occupied[nx][ny] and not visited[nx][ny]:
                heappush(pq, (d+1, nx, ny))

print(dijkstra())
