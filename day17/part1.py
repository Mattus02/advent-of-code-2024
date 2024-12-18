reg = {}
reg[4] = 729
reg[5] = 0
reg[6] = 0

program = [0,1,5,4,3,0]

ip = 0

output = []

while ip < len(program):
    instr = program[ip]
    op = program[ip+1]
    literal = True
    if op in reg:
        literal = False

    if instr == 0:
        op = 2 ** op if literal else 2 ** reg[op]
        reg[4] = int(reg[4] / op)
    elif instr == 1:
        reg[5] = reg[5] ^ op
    elif instr == 2:
        op = op if literal else reg[op]
        reg[5] = op % 8
    elif instr == 3:
        if not reg[4] == 0:
            ip = op
            continue
    elif instr == 4:
        reg[5] = reg[5] ^ reg[6]
    elif instr == 5:
        op = op if literal else reg[op]
        output.append(op % 8)
    elif instr == 6:
        op = 2 ** op if literal else 2 ** reg[op]
        reg[5] = int(reg[4] / op)
    elif instr == 7:
        op = 2 ** op if literal else 2 ** reg[op]
        reg[6] = int(reg[4] / op)

    ip += 2

print(','.join(map(str, output)))