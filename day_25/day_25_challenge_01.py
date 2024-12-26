def process_lock(lock):
    total_rows = len(lock)
    total_columns = len(lock[0])
    lock_comb = []
    for i in range(total_columns):
        for j in range(1, total_rows):
            if lock[j][i] == '.':
                lock_comb.append(j-1)
                break
    return tuple(lock_comb)

def proces_key(key):
    total_rows = len(key)
    total_columns = len(key[0])
    key_comb = []
    for i in range(total_columns):
        for j in range(1, total_rows):
            if key[j][i] == '#':
                key_comb.append(total_rows-j-1)
                break
    return tuple(key_comb)


def load_data():
    with open('input_25.txt') as file:
        sections = file.read().split('\n\n')
        keys = []
        locks = []
        for section in sections:
            lines = section.splitlines()
            if lines[0][0] == '#':
                locks.append(process_lock(lines))
            else:
                keys.append(proces_key(lines))
    return keys, locks

def is_match(key,lock):
    for i in range(len(key)):
        if key[i] + lock[i] > 5:
            return False
    return True

def main():
    keys,locks = load_data()
    total = 0
    for lock in locks:
        for key in keys:
            total += 1 if is_match(key,lock) else 0
    print(total)

main()