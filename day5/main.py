################################
# Common first stage
################################

before = {}
for n in range(1, 100):
    before[n] = set()

updates = []

with open("input.txt") as file:
    while True:
        line = file.readline()
        if not line.strip():
            break
        a, b = map(int, line.split('|'))
        before[b].add(a)
    
    while True:
        line = file.readline()
        if not line:
            break
        updates.append(list(map(int, line.split(','))))

################################
# Common function
################################

def areOrdered(pages):
    for i in range(len(pages)):
        for j in range(i+1, len(pages)):
            if pages[j] in before[pages[i]]:
                return False
    return True

################################
# Part 1
################################

result = 0
for pages in updates:
    if areOrdered(pages):
        result += pages[len(pages) // 2]
print(result)

################################
# Part 2
################################

def orderPages(pages):
    result = []
    while len(pages) > 0:
        for page in pages:
            canAdd = True
            for otherPage in before[page]:
                if otherPage in pages and otherPage not in result:
                    canAdd = False
                    break
            if canAdd:
                result.append(page)
                break
        pages.remove(result[-1])
    return result

result = 0
for pages in updates:
    if not areOrdered(pages):
        orderedPages = orderPages(pages)
        result += orderedPages[len(orderedPages) // 2]
print(result)