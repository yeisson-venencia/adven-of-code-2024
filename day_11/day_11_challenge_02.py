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

def initialize_stone_book(stone_line, blinks):
    stone_book = dict()
    for stone in stone_line:
        stone_key = f"{blinks}-{stone}"
        if stone_key not in stone_book.keys():
            stone_book[stone_key] = 1
        else:
            stone_book[stone_key] += 1
    return stone_book

def downgrade_stone_book(stone_book):
    original_keys = [x for x in stone_book.keys()]
    for stone_key in original_keys:
        components = stone_key.split('-')
        stone_age = int(components[0])
        stone_id = components[1]
        stone_fragments = split_stone(stone_id)
        for fragment in stone_fragments:
            new_stone_key = f"{stone_age - 1}-{fragment}"
            if new_stone_key not in stone_book.keys():
                stone_book[new_stone_key] = stone_book[stone_key]
            else:
                stone_book[new_stone_key] += stone_book[stone_key]
        stone_book.pop(stone_key)

def valuate_stone_book(stone_book):
    print(f"Different stones : {len(stone_book.keys())}")
    total_stones = 0
    for stone_key in stone_book.keys():
        total_stones += stone_book[stone_key]
    print(f"Total stones : {total_stones}")

def main():
    stone_line = load_data()
    blinks = 75
    stone_book = initialize_stone_book(stone_line, blinks)
    while blinks > 0:
        downgrade_stone_book(stone_book)
        blinks -= 1
    valuate_stone_book(stone_book)

main()