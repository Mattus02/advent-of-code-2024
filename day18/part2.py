# Lazy solution

occupied = [[False for _ in range(71)] for _ in range(71)]

def dfs():
    visited = [[False for _ in range(71)] for _ in range(71)]
    visited[0][0] = True
    stack = [(0, 0, 0)]
    while len(stack) > 0:

        d, x, y = stack.pop()

        if x == 70 and y == 70:
            return d

        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if nx >= 0 and nx < 71 and ny >= 0 and ny < 71 and not occupied[nx][ny] and not visited[nx][ny]:
                stack.append((d+1, nx, ny))
                visited[nx][ny] = True

    return -1

file = open("input.txt")
i = 1
while True:
    print(i)
    x, y = map(int, file.readline().strip().split(','))
    occupied[x][y] = True

    if dfs() == -1:
        print(x, y)
        break
    i += 1