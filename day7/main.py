from itertools import product
from copy import deepcopy

OpPlus = 0
OpMult = 1
OpConc = 2

def evaluate(operands, operators):
    operands = deepcopy(operands)
    for i in range(len(operators)):
        operator = operators[i]
        a, b = operands[i], operands[i+1]
        res = None
        if operator == OpPlus:
            res = a+b
        elif operator == OpMult:
            res = a*b
        else:
            res = int(str(a) + str(b))
        operands[i+1] = res
    return operands[-1]

answer = 0
with open("input.txt") as file:
    for line in file:
        result, operands = line.split(':')
        result = int(result)
        operands = list(map(int, operands.strip().split()))

        for permutation in product([OpPlus, OpMult], repeat=len(operands)-1):
            evaluation = evaluate(operands, permutation)
            if evaluation == result:
                answer += evaluation
                break

print("Part 1:", answer)

answer = 0
with open("input.txt") as file:
    for line in file:
        result, operands = line.split(':')
        result = int(result)
        operands = list(map(int, operands.strip().split()))

        for permutation in product([OpPlus, OpMult, OpConc], repeat=len(operands)-1):
            evaluation = evaluate(operands, permutation)
            if evaluation == result:
                answer += evaluation
                break
    
print("Part 2:", answer)