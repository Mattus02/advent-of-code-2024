# Solved by manual inspection
# File contains functions that i used in the Python REPL to solve the problem
# Spoilers/hints ahead

# Start by adding 0b1+0b1, 0b10+0b10, 0b100+0b100, and so on and inspect the output 
# to see when the adder misbehaves. (See simulate() and printz() functions below)

# When the adder misbehaves and there is some output bit which should be set to 1 but isn't,
# then inspect the output gate compare it to other outputs which are behaving correctly. (See printo() function below)

# When you suspect that you have found an issue, swap() the outputs and check if it solved the problem.

file = open('input2.txt')

wire = dict()
while True:
    line = file.readline().strip()
    if not line:
        break
    w, v = line[:3], int(line[5:])
    wire[w] = v
    # Input values don't really matter, since we will create our own inputs

gates = []
while True:
    line = file.readline().strip().split()
    if not line:
        break
    gates.append((line[0], line[1], line[2], line[4]))

# Print the output in binary
def printz():
    z = 0
    for i in range(46):
        s = 'z'+str(i).zfill(2)
        z += wire[s] * 2 ** i
    print(bin(z))

def simulate(X, Y):
    # Prepare input bits and reset output
    for i in range(46):
        wire['x'+str(i).zfill(2)] = 1 if (X & (1 << i)) else 0
        wire['y'+str(i).zfill(2)] = 1 if (Y & (1 << i)) else 0
        wire['z'+str(i).zfill(2)] = 0

    # Set wire values
    g = gates.copy()
    while len(g) > 0:
        to_delete = []
        for i, gate in enumerate(g):
            a, op, b, r = gate[0], gate[1], gate[2], gate[3]
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
            del g[i]

    printz()

# Print/visualize the inputs of a certain output
def printo(output, depth=0):
    if depth > 4:
        return
    if output in depend:
        op, a, b = depend[output]
        print('    '*depth, output, '=', op, a, b)
        printo(a, depth+1)
        printo(b, depth+1)
    else:
        print('    '*depth, output)

# Get the value of a bit
def get(output):
    return wire[output]

# Swap outputs
def swap(out1, out2):
    for i, (a, op, b, out) in enumerate(gates):
        if out == out1:
            gates[i] = (a, op, b, out2)
        elif out == out2:
            gates[i] = (a, op, b, out1)