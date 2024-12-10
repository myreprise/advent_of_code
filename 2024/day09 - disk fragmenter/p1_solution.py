
def parse_disk_map(disk_map):
    blocks = []
    file_id = 0
    is_file = True
    for length in map(int, disk_map):
        if is_file:
            blocks.extend([file_id] * length)
            if length > 0:
                file_id += 1
        else:
            blocks.extend(['.'] * length)
        is_file = not is_file
    return blocks

def compact_disk(blocks):
    while '.' in blocks:
        last_file_idx = len(blocks) - 1 - blocks[::-1].index(next(b for b in reversed(blocks) if b != '.'))

        first_free_idx = blocks.index(".")
        if first_free_idx < last_file_idx:
            blocks[first_free_idx] = blocks[last_file_idx]
            blocks[last_file_idx] = '.'
        else:
            break
    return blocks

def calculate_checksum(blocks):
    checksum = 0
    for idx, block in enumerate(blocks):
        if block != '.':
            checksum += idx * block
    return checksum

def parse_input(filename):
    with open(filename, 'r') as file:
        disk_map = file.read().strip()
        return disk_map


filename = 'input.txt'
disk_map = parse_input(filename)
print('disk map:')
print(f'disk map: {disk_map}')

blocks = parse_disk_map(disk_map=disk_map)
print('\nblocks')
print(blocks)

compacted_blocks = compact_disk(blocks)
print('\ncompacted blocks')
print(compacted_blocks)

checksum = calculate_checksum(compacted_blocks)
print('checksum')
print(checksum)
# answer is 6378826667552
