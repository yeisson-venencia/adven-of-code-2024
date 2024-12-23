def load_data():
    with open('input_22.txt') as file:
        lines = file.read().splitlines()
        data = [int(x) for x in lines]
    return data

def mix(value,secret):
    return value ^ secret

def prune(secret):
    return secret % 16777216

def evolve(secret):
    secret = prune( mix(secret*64,secret))
    secret = prune( mix(secret // 32,secret))
    secret = prune( mix(secret * 2048,secret))

    return secret

def generate_change_seq_dict(secret):
    changes = []
    changes_dict = dict()
    old_secret = secret
    for i in range(2000):
        new_secret = evolve(old_secret)
        osp = old_secret % 10
        nsp = new_secret % 10
        changes.append(nsp-osp)
        old_secret = new_secret
        if i > 2:
            seq = (changes[i-3],changes[i-2],changes[i-1], changes[i])
            if seq not in changes_dict:
                changes_dict[seq] = nsp
    return changes_dict

def main():
    data = load_data()
    seq_dict = dict()
    for secret in data:
        secret_seq_dict = generate_change_seq_dict(secret)
        for key,value in secret_seq_dict.items():
            if key not in seq_dict:
                seq_dict[key] = value
            else:
                seq_dict[key] += value

    best_total = 0
    best_seq = None
    for key,value in seq_dict.items():
        if value > best_total:
            best_total = value
            best_seq = key
    print(best_total)
    print(best_seq)

main()