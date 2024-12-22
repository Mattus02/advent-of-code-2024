MOD = 16777216

def NextSecret(secret):
    secret = (secret ^ (secret * 64)) % MOD
    secret = (secret ^ (secret // 32)) % MOD
    secret = (secret ^ (secret * 2048)) % MOD
    return secret

answer = 0
for number in open("input1.txt").readlines():
    number = int(number)
    for _ in range(2000):
        number = NextSecret(number)
    answer += number
print(answer)