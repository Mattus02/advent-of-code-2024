def solve(ax, ay, bx, by, px, py):
    d, r = divmod(py * ax - px * ay, by * ax - ay * bx)
    if r != 0:
        return 0
    B = d
    d, r = divmod(px * by - py * bx, ax * by - bx * ay)
    if r != 0:
        return 0
    A = d
    return A*3 + B

file = open("input.txt")

answer = 0
while True:
    ALine = file.readline().strip().split()
    ax = int(ALine[2].split('+')[1][:-1])
    ay = int(ALine[3].split('+')[1])

    BLine = file.readline().strip().split()
    bx = int(BLine[2].split('+')[1][:-1])
    by = int(BLine[3].split('+')[1])

    PLine = file.readline().strip().split()
    px = int(PLine[1].split('=')[1][:-1])
    py = int(PLine[2].split('=')[1])

    res = solve(ax, ay, bx, by, px + 10000000000000, py + 10000000000000)
    if res != 0:
        answer += res

    if not file.readline():
        break
    
print(answer)
