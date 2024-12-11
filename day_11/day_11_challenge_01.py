def load_data():
    with open('input_11.txt') as file:
        line = file.readline()
        data = line.split()
    return data

def split_stone(stone):
    if int(stone) == 0:
        return ['1']
    if len(stone) % 2 == 0:
        middle_index = int(len(stone) / 2)
        return [f"{stone[:middle_index]}", f"{int(stone[middle_index:])}"]
    else:
        return [f"{int(stone) * 2024}"]

def evolve_stone_line(stone_line):
    new_stone_line = []
    for stone in stone_line:
        stone_fragments = split_stone(stone)
        for fragment in stone_fragments:
            new_stone_line.append(fragment)
    return new_stone_line


def main():
    stone_line = load_data()
    blinks = 25
    while blinks > 0:
        stone_line = evolve_stone_line(stone_line)
        blinks -= 1
    print(len(stone_line))

main()