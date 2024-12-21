

def parse_input(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    return [l.strip() for l in lines]

def parse_reindeer_lines(reindeer_lines):
    reindeer_stats = []
    for line in reindeer_lines:
        parts = line.split()
        name = parts[0]
        speed = int(parts[3])
        fly_time = int(parts[6])
        rest_time = int(parts[13])
        reindeer_stats.append((name, speed, fly_time, rest_time))

    return reindeer_stats


def calculate_distance(speed, fly_time, rest_time, total_seconds):
    """
    Calculate complete cycles of flying and resting
    """
    cycle_time = fly_time + rest_time
    full_cycles = total_seconds // cycle_time
    remaining_time = total_seconds % cycle_time

    # Calculate total flying time
    flying_time = full_cycles * fly_time + min(remaining_time, fly_time)

    # Calculate total distance
    return flying_time * speed

def find_winning_reindeer(reindeer_stats, race_duration):
    distances = {}
    for name, speed, fly_time, rest_time in reindeer_stats:
        distances[name] = calculate_distance(speed, fly_time, rest_time, race_duration)

    # Find the maximum distance
    return  max(distances.values())

filename = 'input.txt'
race_duration = 2503

reindeer_lines = parse_input(filename=filename)
reindeer_stats = parse_reindeer_lines(reindeer_lines=reindeer_lines)
result = find_winning_reindeer(reindeer_stats=reindeer_stats, race_duration=race_duration)
print(result)
# answer is 2660
