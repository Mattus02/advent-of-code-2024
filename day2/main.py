
def IsSafe(levels):
    if levels[0] == levels[1]:
        return False
    increasing = levels[0] < levels[1]
    left = levels[0]
    for i in range(1, len(levels)):
        diff = abs(levels[i] - left)
        if diff < 1 or diff > 3:
            return False
        if (increasing and levels[i] < left) or (not increasing and levels[i] > left):
            return False
        left = levels[i]
    return True

def part1():
    with open("input.txt", "r") as file:
        result = 0
        for line in file:
            levels = list(map(int, line.split()))
            if IsSafe(levels):
                result += 1
        print(result)

def part2():
    with open("input.txt", "r") as file:
        result = 0
        for line in file:
            levels = list(map(int, line.split()))
            if IsSafe(levels):
                result += 1
                continue
            for i in range(len(levels)):
                tmpList = levels[:i] + levels[i+1:]
                if IsSafe(tmpList):
                    result += 1
                    break
    print(result)

part1()
part2()