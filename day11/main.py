cache = {}

def count(stone, depth):
    if (stone, depth) in cache:
        return cache[(stone, depth)]
    if depth == 0:
        return 1
    result = None
    if stone == 0:
        result = count(1, depth - 1)
    elif len(str(stone)) % 2 == 0:
        stoneStr = str(stone)
        l = len(stoneStr)
        result = count(int(stoneStr[:l//2]), depth - 1) + count(int(stoneStr[l//2:]), depth - 1)
    else:
        result = count(stone * 2024, depth - 1)
    cache[(stone, depth)] = result
    return result

file = open("self-made-input.txt")
stones = list(map(int, file.read().split()))

answer1 = 0
answer2 = 0

for stone in stones:
    answer1 += count(stone, 25)
    answer2 += count(stone, 75)

print("Part1:", answer1)
print("Part1:", answer2)