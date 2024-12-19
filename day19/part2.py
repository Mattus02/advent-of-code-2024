file = open("input.txt")
patterns = file.readline().strip().split(", ")
file.readline()

cache = {}

def Count(design):
    if len(design) == 0:
        return 1

    if not design in cache:
        cache[design] = 0
        for pattern in patterns:
            if len(design) >= len(pattern) and design[:len(pattern)] == pattern:
                cache[design] += Count(design[len(pattern):])

    return cache[design]

answer = 0
while True:
    design = file.readline().strip()
    if not design:
        break
    answer += Count(design)

print(answer)