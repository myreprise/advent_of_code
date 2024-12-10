

def parse_disk_map(disk_map):
    """
    Convert the disk map to a list of file blocks and free spaces
    """
    file_lengths = []
    free_lengths = []

    for i in range(0, len(disk_map), 2):
        file_lengths.append(int(disk_map[i]))
        if i+1 < len(disk_map):
            free_lengths.append(int(disk_map[i+1]))
    
    return file_lengths, free_lengths


def compact_files(file_lengths, free_lengths):
    """
    Simulate the movement of files to the leftmost available spaces
    """
    # Create the initial disk state
    disk = []
    for file_length, free_length in zip(file_lengths, free_lengths):
        disk.extend([str(file_lengths.index(file_length))] * file_length)
        disk.extend(['.'] * free_length)

    compacted_disk = []
    for file_id in range(len(file_lengths)):
        # Append all blocks for this file, one by one
        compacted_disk.extend([str(file_id)] * file_lengths[file_id])
    
    compacted_disk.extend(['.'] * len(compacted_disk),)

    return compacted_disk


def calculate_checksum_from_disk_map(disk_map):
    checksum = 0
    for position, block in enumerate(disk_map):
        if block.isdigit():
            checksum += position * int(block)
    return checksum


def solve(disk_map):
    file_lengths, free_lengths = parse_disk_map(disk_map)
    compacted_disk = compact_files(file_lengths, free_lengths)
    return calculate_checksum_from_disk_map(compacted_disk)



with open('test_input.txt', 'r') as file:
    disk_map = file.read()

disk_map = "".join(char for char in disk_map if char.isdigit() or char == '.')

result = solve(disk_map)
print(result)