from collections import defaultdict
import itertools

conn = defaultdict(list)

for line in open('input.txt').read().split('\n'):
    a, b = line.split('-')
    conn[a].append(b)
    conn[b].append(a)

triples = set()
for computer, connections in conn.items():
    if computer[0] != 't':
        continue
    for a, b in list(itertools.combinations(connections, 2)):
        if b in conn[a]:
            triples.add('-'.join(sorted([computer, a, b])))

print(len(triples))