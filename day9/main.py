
FREE = -1

expanded = []

with open("input.txt") as file:
    input = file.readline()
    print(input)
    id = 0
    for i in range(len(input)):
        if i % 2 == 0:
            expanded += str(id) * int(input[i]) 