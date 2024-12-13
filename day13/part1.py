INF = 99999999

def solve(ax, ay, bx, by, px, py):
    best = INF
    for a in range(101):
        for b in range(101):
            if (a * ax + b * bx, a * ay + b * by) == (px, py):
                best = a * 3 + b
    return 0 if best == INF else best

file = open("input.txt")

answer = 0
while True:
    ALine = file.readline().strip().split()
    Adx = int(ALine[2].split('+')[1][:-1])
    Ady = int(ALine[3].split('+')[1])

    BLine = file.readline().strip().split()
    Bdx = int(BLine[2].split('+')[1][:-1])
    Bdy = int(BLine[3].split('+')[1])

    PLine = file.readline().strip().split()
    Px = int(PLine[1].split('=')[1][:-1])
    Py = int(PLine[2].split('=')[1])

    answer += solve(Adx, Ady, Bdx, Bdy, Px, Py)

    if not file.readline():
        break

print(answer)