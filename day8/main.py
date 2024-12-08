ROWS = 0
COLS = 0

freqs = {}

with open("input.txt") as file:
    for line in file:
        line = line.strip()
        ROWS += 1
        COLS = len(line)
        for col, c in enumerate(line):
            if c != '.':
                if c not in freqs:
                    freqs[c] = []
                freqs[c].append((ROWS - 1, col))

def withinBounds(r, c):
    return r >= 0 and r < ROWS and c >= 0 and c < COLS

antinodes = set()

def addAntinodes(a1, a2, part2):
    if part2:
        antinodes.add(a1)
        antinodes.add(a2)
    r1, c1 = a1
    r2, c2 = a2

    dr, dc = r1 - r2, c1 - c2
    rNew, cNew = r2 + 2*dr, c2 + 2*dc
    if part2:
        while withinBounds(rNew, cNew):
            antinodes.add((rNew, cNew))
            rNew += dr
            cNew += dc
    else:
        if withinBounds(rNew, cNew):
            antinodes.add((rNew, cNew))

    rNew, cNew = r1 - 2*dr, c1 - 2*dc
    if part2:
        while withinBounds(rNew, cNew):
            antinodes.add((rNew, cNew))
            rNew -= dr
            cNew -= dc
    else:
        if withinBounds(rNew, cNew):
            antinodes.add((rNew, cNew))

for freq in freqs:
    antennas = freqs[freq]
    for i in range(len(antennas)):
        for j in range(i+1, len(antennas)):
            addAntinodes(antennas[i], antennas[j], False)

print("Part 1:", len(antinodes))
antinodes.clear()

for freq in freqs:
    antennas = freqs[freq]
    for i in range(len(antennas)):
        for j in range(i+1, len(antennas)):
            addAntinodes(antennas[i], antennas[j], True)

print("Part 2:", len(antinodes))