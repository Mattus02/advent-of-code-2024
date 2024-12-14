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

positions = []
for i in range(len(robots)):
    p, v = robots[i]
    x = (p[0] + 100 * v[0]) % WIDTH
    y = (p[1] + 100 * v[1]) % HEIGHT
    positions.append((x, y))

qs = [0, 0, 0, 0]

for x, y in positions:
    if x == WIDTH // 2 or y == HEIGHT // 2:
        continue
    q = 0
    if x > WIDTH // 2:
        q += 1
    if y > HEIGHT // 2:
        q += 2
    qs[q] += 1

answer = 1
for q in qs:
    answer *= q

print(answer)