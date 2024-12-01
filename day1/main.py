def part1():
    list1 = []
    list2 = []

    with open("input.txt", "r") as file:
        for line in file:
            a, b = map(int, line.split())
            list1.append(a)
            list2.append(b)

    list1.sort()
    list2.sort()

    result = 0

    for i in range(len(list1)):
        result += abs(list1[i] - list2[i])

    print(result)


def part2():
    list1 = []
    occurrences = {}

    with open("input.txt", "r") as file:
        for line in file:
            a, b = map(int, line.split())
            list1.append(a)
            if b not in occurrences:
                occurrences[b] = 0
            occurrences[b] += 1

    result = 0
    for n in list1:
        if n not in occurrences:
            continue
        result += n * occurrences[n]

    print(result)


part1()
part2()