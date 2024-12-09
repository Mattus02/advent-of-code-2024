
FREE = -1

fsystem = []

with open("input.txt") as file:
    input = file.readline()
    print(input)
    id = 0
    for i in range(len(input)):
        repeat = int(input[i])
        if i % 2 == 0:
            fsystem.append((id, repeat))
            id += 1
        else:
            fsystem.append((FREE, repeat))

print(fsystem)

end = len(fsystem) - 1
while fsystem[end][0] == FREE:
    end -= 1

def findLargeEnoughSpan(min):
    for i in range(len(fsystem)):
        if fsystem[i][1] >= min:
            return i
    return -1

while end >= 0:
    id, repeat = fsystem[end]
    i = findLargeEnoughSpan(repeat)
    if i != -1:
        diff = fsystem[i][1] - repeat
        fsystem.insert(i + 1, (FREE, diff))
        fsystem[i] = (id, repeat)
        fsystem[end] = (FREE, repeat)
    while end >= 0 and fsystem[end][0] == FREE:
        end -= 1

print(fsystem)

answer = 0
for i in range(len(fsystem)):
    if fsystem[i][0] != FREE:
        answer += fsystem[i][0] * i

print(answer)

# while start < end:
#     expanded[start] = expanded[end]
#     expanded[end] = '.'
#     while expanded[end] == '.':
#         end -= 1
#     while expanded[start] != '.':
#         start += 1

# print(expanded)

# answer = 0
# i = 0
# while expanded[i] != '.':
#     answer += expanded[i] * i
#     i += 1

# print(answer)