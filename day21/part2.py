# Ugly code, sorry

import itertools

numpadKeyToCoord = {'A':(3,2),'0':(3,1),'1':(2,0),'2':(2,1),'3':(2,2),'4':(1,0),'5':(1,1),'6':(1,2),'7':(0,0),'8':(0,1),'9':(0,2)}

PATHS = dict()
for key in ['^', 'A', '<', 'v', '>']:
    PATHS[key] = dict()
PATHS['A']['A'] = ['']
PATHS['A']['^'] = ['<']
PATHS['A']['>'] = ['v']
PATHS['A']['v'] = ['v<', '<v']
PATHS['A']['<'] = ['<v<', 'v<<']
PATHS['^']['A'] = ['>']
PATHS['^']['^'] = ['']
PATHS['^']['>'] = ['v>', '>v']
PATHS['^']['v'] = ['v']
PATHS['^']['<'] = ['v<']
PATHS['>']['A'] = ['^']
PATHS['>']['^'] = ['<^', '^<']
PATHS['>']['>'] = ['']
PATHS['>']['v'] = ['<']
PATHS['>']['<'] = ['<<']
PATHS['v']['A'] = ['>^', '^>']
PATHS['v']['^'] = ['^']
PATHS['v']['>'] = ['>']
PATHS['v']['v'] = ['']
PATHS['v']['<'] = ['<']
PATHS['<']['A'] = ['>>^', '>^>']
PATHS['<']['^'] = ['>^']
PATHS['<']['>'] = ['>>']
PATHS['<']['v'] = ['>']
PATHS['<']['<'] = ['']

keypadDiff = {'^':(-1,0),'<':(0,-1),'v':(1,0),'>':(0,1), 'A':(0, 0)}

def GetAllNumpadPaths(r, c, tr, tc):
    dr = tr - r
    dc = tc - c
    vertical = 'v' * max(dr, 0) + '^' * max(-dr, 0)
    horizontal = '>' * max(dc, 0) + '<' * max(-dc, 0)
    moves = vertical + horizontal
    paths = set(itertools.permutations(moves))
    paths = [''.join(list(path) + ['A']) for path in paths]

    # Remove paths that cross empty area
    pathsToRemove = []
    rsave, csave = r, c
    for i, path in enumerate(paths):
        r, c = rsave, csave
        for key in path:
            dr, dc = keypadDiff[key]
            r, c = r + dr, c + dc
            if r == 3 and c == 0:
                pathsToRemove.append(i)
    for i in reversed(pathsToRemove):
        del paths[i]

    return paths

cache = dict()

def Cost(keyFrom, keyTo, layer):
    if layer == 1:
        return len(PATHS[keyFrom][keyTo][0]) + 1 # +1 for the 'A'

    if (keyFrom, keyTo, layer) not in cache:
        best = float('inf')
        for path in PATHS[keyFrom][keyTo]:
            path = 'A' + path + 'A'
            costs = [Cost(path[i], path[i+1], layer-1) for i in range(len(path) - 1)]
            best = min(best, sum(costs))
        cache[(keyFrom, keyTo, layer)] = best
    return cache[(keyFrom, keyTo, layer)]

answer = 0
for line in open("input.txt").read().split('\n'):
    line = 'A' + line

    numpadPaths = []
    for i in range(len(line) - 1):
        r, c = numpadKeyToCoord[line[i]]
        tr, tc = numpadKeyToCoord[line[i+1]]
        numpadPaths.append(GetAllNumpadPaths(r, c, tr, tc))
    numpadPaths = ['A' + ''.join(l) for l in list(itertools.product(*numpadPaths))]

    best = float('inf')
    for path in numpadPaths:
        cost = 0
        for i in range(len(path) - 1):
            cost += Cost(path[i], path[i+1], 25)
        best = min(best, cost)
    answer += best * int(line[1:-1])

print(answer)