def load_disk_map():
    with open('input_09.txt') as input_file:
        data = input_file.read()
    return data

def add_elements_to_block_map(block_map,  element, element_length):
    for _ in range(element_length):
        block_map.append(element)

def generate_block_map(disk_map):
    block_map = []
    current_digit_represent = 'File'
    current_file_id = 0
    for digit in disk_map:
        element_to_insert = str(current_file_id) if current_digit_represent == 'File' else '.'
        add_elements_to_block_map(block_map,  element_to_insert, int(digit))
        if current_digit_represent == 'File':
            current_digit_represent = 'Space'
            current_file_id += 1
        else:
            current_digit_represent = 'File'
    return block_map

def is_file_block(block):
    return not block == '.'

def fragment_disk(block_map):
    left_pointer = 0
    right_pointer = len(block_map) - 1
    while left_pointer <= right_pointer:
        left_pointer_block = block_map[left_pointer]
        right_pointer_block = block_map[right_pointer]
        if is_file_block(right_pointer_block) and not is_file_block(left_pointer_block):
            temporal = left_pointer_block
            block_map[left_pointer] = right_pointer_block
            block_map[right_pointer] = temporal
            left_pointer += 1
            right_pointer -= 1
        else:
            if not is_file_block(right_pointer_block):
                right_pointer -= 1
            if is_file_block(left_pointer_block):
                left_pointer += 1

def calculate_filesystem_checksum(block_map):
    checksum = 0
    for index,block in enumerate(block_map):
        if not is_file_block(block):
            break
        checksum += index * int(block)
    return checksum

def main():
    disk_map = load_disk_map()
    block_map = generate_block_map(disk_map)
    fragment_disk(block_map)
    print(f"Filesystem checksum = {calculate_filesystem_checksum(block_map)}")

main()