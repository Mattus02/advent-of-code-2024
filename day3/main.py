# I didn't feel like learning regex today either :)

def findMul(substr):
    l = len(substr)
    i = substr.find("mul(")
    if i == -1:
        return -1, -1
    i = i + 4
    substr = substr[i:]
    comma = substr.find(",")
    endp = substr.find(")")
    if comma == -1 or endp == -1:
        return -1, -1
    if endp < comma:
        return i, -1
    slice1 = substr[:comma]
    slice2 = substr[comma+1:endp]
    if slice1.isdigit() and slice2.isdigit():
        a = int(slice1)
        b = int(slice2)
        return i + endp + 1, a*b
    else:
        return i, -1

def processLine(line):
    result = 0
    while True:
        i, n = findMul(line)
        if i == -1:
            break
        if n != -1:
            result += n
        line = line[i:]
    return result

def preProcessLine(line, enabled):
    substrings = []
    while True:
        if enabled:
            i = line.find("don't()")
            if i == -1:
                substrings.append(line)
                break
            substrings.append(line[:i])
            line = line[i+7:]
            enabled = False
        else:
            i = line.find("do()")
            if i == -1:
                break
            line = line[i+4:]
            enabled = True
    return "".join(substrings), enabled            

def part1():
    result = 0
    with open("input.txt") as file:
        for line in file:
            result += processLine(line)
        print(result)

def part2():
    result = 0
    with open("input2.txt") as file:
        enabled = True
        for line in file:
            line, enabled = preProcessLine(line, enabled)
            result += processLine(line)
        print(result)

part1()
part2()