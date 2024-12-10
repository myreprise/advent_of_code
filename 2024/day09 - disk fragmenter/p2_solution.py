def parse_input(filename):
    with open(filename, 'r') as file:
        disk_map = file.read().strip()
        return disk_map

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

def find_free_span(blocks, length):
    free_start = -1
    free_length = 0
    for i, block in enumerate(blocks):
        if block == '.':
            if free_start == -1:
                free_start = i
            free_length += 1
            if free_length == length:
                return free_start
        else:
            free_start = -1
            free_length = 0
    return None

def compact_disk_by_file(blocks):
    """Compact the disk by moving whole files."""
    file_ids = sorted(set(b for b in blocks if b != '.'), reverse=True)  # Get all file IDs in reverse order
    for file_id in file_ids:
        # Get all blocks of the current file
        file_positions = [i for i, b in enumerate(blocks) if b == file_id]
        if not file_positions:
            continue
        file_length = len(file_positions)
        # Find the leftmost span of free space that can fit this file
        free_start = find_free_span(blocks, file_length)
        if free_start is not None and free_start < min(file_positions):
            # Move the file to the free space
            for i in range(file_length):
                blocks[free_start + i] = file_id
                blocks[file_positions[i]] = '.'
    return blocks

def calculate_checksum(blocks):
    """Calculate the checksum of the final compacted disk."""
    checksum = 0
    for idx, block in enumerate(blocks):
        if block != '.':
            checksum += idx * block
    return checksum

filename = 'input.txt'
disk_map = parse_input(filename)
print('disk map:')
print(f'disk map: {disk_map}')

# Main logic
blocks = parse_disk_map(disk_map)
print('blocks:')
print(blocks)

compacted_blocks = compact_disk_by_file(blocks)
print('compacted blocks')
print(compacted_blocks)

checksum = calculate_checksum(compacted_blocks)
print('checksum')
print(checksum)
# answer is 6413328569890
