def load_disk_map():
    with open('input_09.txt') as input_file:
        data = input_file.read()
    return data

def add_elements_to_block_map(block_map,  element, element_length):
    for _ in range(element_length):
        block_map.append(element)

def generate_block_map(disk_map):
    block_map = []
    free_space_map = []
    file_map = []
    current_digit_represent = 'File'
    current_file_id = 0
    for digit in disk_map:
        element_to_insert = str(current_file_id) if current_digit_represent == 'File' else '.'

        if current_digit_represent == 'File':
            if int(digit) > 0:
                file_map.append((element_to_insert,len(block_map), int(digit)))
            current_digit_represent = 'Space'
            current_file_id += 1
        else:
            if int(digit) > 0:
                free_space_map.append((len(block_map),int(digit)))
            current_digit_represent = 'File'

        add_elements_to_block_map(block_map, element_to_insert, int(digit))
    return block_map, free_space_map, file_map

def file_fit_on_space(file_data, space_data):
    return space_data[1] >= file_data[2]

def is_file_swappable(file_data, space_data):
    return space_data[0] < file_data[1]

def move_file(block_map, space_data, file_data):
    for index in range(file_data[2]):
        block_map[space_data[0] + index] = file_data[0]
        block_map[file_data[1] + index] = '.'

def update_free_space_map(free_space_map, space_data_index, block_weight):
    space_data = free_space_map[space_data_index]
    updated_space_data = (space_data[0]+block_weight, space_data[1]-block_weight)
    if updated_space_data[1] == 0:
        free_space_map.pop(space_data_index)
    else:
        free_space_map[space_data_index] = updated_space_data

def fragment_disk(block_map, free_space_map, file_map):
    file_map.reverse()
    for file_data in file_map:
        for index,space_data in enumerate(free_space_map):
            if not is_file_swappable(file_data, space_data):
                break
            if file_fit_on_space(file_data, space_data):
                move_file(block_map, space_data, file_data)
                update_free_space_map(free_space_map, index,  file_data[2])
                break

def is_file_block(block):
    return not block == '.'

def calculate_filesystem_checksum(block_map):
    checksum = 0
    for index,block in enumerate(block_map):
        if is_file_block(block):
            checksum += index * int(block)
    return checksum

def main():
    disk_map = load_disk_map()
    block_map, free_space_map, file_map = generate_block_map(disk_map)
    fragment_disk(block_map, free_space_map, file_map)
    print(f"Filesystem checksum = {calculate_filesystem_checksum(block_map)}")

main()