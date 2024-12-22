from collections import deque

MOD = 16777216

def NextSecret(secret):
    secret = (secret ^ (secret * 64)) % MOD
    secret = (secret ^ (secret // 32)) % MOD
    secret = (secret ^ (secret * 2048)) % MOD
    return secret

seqs = []
for number in open("input2.txt").readlines():
    number = int(number)
    seqs.append(dict())

    history = deque()
    history.append((number % 10, None))
    for i in range(2000):
        number = NextSecret(number)
        price = number % 10
        history.append((price, price - history[-1][0]))
        if i >= 3:
            history.popleft()
            seq = (history[0][1], history[1][1], history[2][1], history[3][1])
            if seq not in seqs[-1]:
                seqs[-1][seq] = price

total = dict()
for s in seqs:
    for k, v in s.items():
        if k not in total:
            total[k] = 0
        total[k] += v

seq, value = max(total.items(), key=lambda x: x[1])
print(seq, value)