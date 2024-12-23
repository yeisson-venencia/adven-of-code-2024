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

def main():
    data = load_data()
    result = 0
    for secret in data:
        for _ in range(2000):
            secret = evolve(secret)
        result += secret
    print(result)


main()