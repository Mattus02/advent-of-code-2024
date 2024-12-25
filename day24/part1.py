file = open('input.txt')

wire = dict()

while True:
    line = file.readline().strip()
    if not line:
        break
    w, v = line[:3], int(line[5:])
    wire[w] = v

gates = []
while True:
    line = file.readline().strip()
    if not line:
        break
    gates.append(line.split())

while len(gates) > 0:
    to_delete = []
    for i, gate in enumerate(gates):
        a, op, b, r = gate[0], gate[1], gate[2], gate[4]
        if a in wire and b in wire:
            if op == 'AND':
                wire[r] = wire[a] & wire[b]
            elif op == 'OR':
                wire[r] = wire[a] | wire[b]
            elif op == 'XOR':
                wire[r] = wire[a] ^ wire[b]
            else:
                assert False
            to_delete.append(i)
    for i in reversed(to_delete):
        del gates[i]

answer = 0
for i in range(100):
    s = str(i).zfill(2)
    if 'z'+s in wire:
        answer += wire['z'+s] * 2 ** i
print(answer)