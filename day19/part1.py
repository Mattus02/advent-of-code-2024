file = open("input.txt")
patterns = file.readline().strip().split(", ")
file.readline()

def CanCreate(design):
    if len(design) == 0:
        return True

    for pattern in patterns:
        if len(design) >= len(pattern) and design[:len(pattern)] == pattern:
            if CanCreate(design[len(pattern):]):
                return True
    
    return False
            
answer = 0
while True:
    design = file.readline().strip()
    if not design:
        break
    if CanCreate(design):
        answer += 1

print(answer)