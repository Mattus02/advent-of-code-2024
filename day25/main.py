locks_keys = open('input.txt').read().split('\n\n')
locks = []
keys = []
for lock_or_key in locks_keys:
    is_lock = True
    for r, line in enumerate(lock_or_key.split('\n')):
        if r == 0:
            if line[0] == '.':
                is_lock = False
                keys.append([None, None, None, None, None])
            else:
                locks.append([0, 0, 0, 0, 0])
            continue
        for c in range(5):
            if is_lock:
                if line[c] == '#':
                    locks[-1][c] = r
            else:
                if line[c] == '#' and keys[-1][c] is None:
                    keys[-1][c] = 6 - r

answer = 0
for lock in locks:
    for key in keys:
        fit = True
        for c in range(5):
            if lock[c] + key[c] > 5:
                fit = False
        if fit:
            answer += 1

print(answer)