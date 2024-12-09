expanded = []

with open("input.txt") as file:
    input = file.readline()
    id = 0
    for i in range(len(input)):
        repeat = int(input[i])
        if i % 2 == 0:
            expanded.extend([id] * repeat)
            id += 1
        else:
            expanded.extend(['.'] * repeat)

print(expanded)

start = expanded.index('.')
end = len(expanded) - 1
while expanded[end] == '.':
    end -= 1

while start < end:
    expanded[start] = expanded[end]
    expanded[end] = '.'
    while expanded[end] == '.':
        end -= 1
    while expanded[start] != '.':
        start += 1

print(expanded)

answer = 0
i = 0
while expanded[i] != '.':
    answer += expanded[i] * i
    i += 1

print(answer)