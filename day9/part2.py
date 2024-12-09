FREE = -1

fsystem = []

with open("input.txt") as file:
    input = file.readline()
    id = 0
    for i in range(len(input)):
        repeat = int(input[i])
        if i % 2 == 0:
            fsystem.append((id, repeat))
            id += 1
        else:
            fsystem.append((FREE, repeat))

end = len(fsystem) - 1
while fsystem[end][0] == FREE:
    end -= 1

def findLargeEnoughSpan(min, end):
    for i in range(end):
        if fsystem[i][0] == FREE and fsystem[i][1] >= min:
            return i
    return -1

while end >= 0:
    id, repeat = fsystem[end]
    i = findLargeEnoughSpan(repeat, end)
    if i != -1:
        diff = fsystem[i][1] - repeat
        fsystem[i] = (id, repeat)
        fsystem[end] = (FREE, repeat)
        if diff > 0:
            fsystem.insert(i + 1, (FREE, diff))
    else:
        end -= 1
    while end >= 0 and fsystem[end][0] == FREE:
        end -= 1

answer = 0
i = 0
for id, repeat in fsystem:
    if id != FREE:
        for j in range(i, i + repeat):
            answer += id * j
    i += repeat

print(answer)