from collections import defaultdict

conn = defaultdict(set)
for line in open('input.txt').read().split('\n'):
    a, b = line.split('-')
    conn[a].add(b)
    conn[b].add(a)

largest_clique = set()
def BronKerbosch(R, P, X):
    if len(P) == 0 and len(X) == 0:
        global largest_clique
        if len(R) > len(largest_clique):
            largest_clique = R
        return
    for computer in P.copy():
        BronKerbosch(R | {computer}, P & conn[computer], X & conn[computer])
        P.remove(computer)
        X.add(computer)

BronKerbosch(set(), set(conn.keys()), set())
print(','.join(sorted(largest_clique)))