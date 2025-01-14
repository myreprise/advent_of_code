from itertools import combinations, chain

# Boss stats
BOSS_HIT_POINTS = 109
BOSS_DAMAGE = 8
BOSS_ARMOR = 2

# Player stats
PLAYER_HIT_POINTS = 100

# Shop inventory
WEAPONS = [
    {"name": "Dagger", "cost": 8, "damage": 4, "armor": 0},
    {"name": "Shortsword", "cost": 10, "damage": 5, "armor": 0},
    {"name": "Warhammer", "cost": 25, "damage": 6, "armor": 0},
    {"name": "Longsword", "cost": 40, "damage": 7, "armor": 0},
    {"name": "Greataxe", "cost": 74, "damage": 8, "armor": 0},
]

ARMOR = [
    {"name": "None", "cost": 0, "damage": 0, "armor": 0},
    {"name": "Leather", "cost": 13, "damage": 0, "armor": 1},
    {"name": "Chainmail", "cost": 31, "damage": 0, "armor": 2},
    {"name": "Splintmail", "cost": 53, "damage": 0, "armor": 3},
    {"name": "Bandedmail", "cost": 75, "damage": 0, "armor": 4},
    {"name": "Platemail", "cost": 102, "damage": 0, "armor": 5},
]

RINGS = [
    {"name": "None", "cost": 0, "damage": 0, "armor": 0},
    {"name": "Damage +1", "cost": 25, "damage": 1, "armor": 0},
    {"name": "Damage +2", "cost": 50, "damage": 2, "armor": 0},
    {"name": "Damage +3", "cost": 100, "damage": 3, "armor": 0},
    {"name": "Defense +1", "cost": 20, "damage": 0, "armor": 1},
    {"name": "Defense +2", "cost": 40, "damage": 0, "armor": 2},
    {"name": "Defense +3", "cost": 80, "damage": 0, "armor": 3},
]

# Simulate the battle
def does_player_win(player_hp, player_damage, player_armor, boss_hp, boss_damage, boss_armor):
    player_effective_damage = max(1, player_damage - boss_armor)
    boss_effective_damage = max(1, boss_damage - player_armor)

    # Calculate number of turns to defeat each
    player_turns_to_win = -(-boss_hp // player_effective_damage)
    boss_turns_to_win = -(-player_hp // boss_effective_damage)

    return player_turns_to_win <= boss_turns_to_win

# Generate all combinations of items
def generate_item_combinations():
    for weapon in WEAPONS:
        for armor in ARMOR:
            for ring_combo in chain(combinations(RINGS[1:], 0), combinations(RINGS[1:], 1), combinations(RINGS[1:], 2)):
                yield [weapon, armor, *ring_combo]

# Find the maximum cost where the player loses
def find_maximum_cost_to_lose():
    max_cost = 0

    for items in generate_item_combinations():
        total_cost = sum(item["cost"] for item in items)
        total_damage = sum(item["damage"] for item in items)
        total_armor = sum(item["armor"] for item in items)

        # Check if the player loses
        if not does_player_win(PLAYER_HIT_POINTS, total_damage, total_armor, BOSS_HIT_POINTS, BOSS_DAMAGE, BOSS_ARMOR):
            max_cost = max(max_cost, total_cost)

    return max_cost

# Execute the solution
result = find_maximum_cost_to_lose()
print(result)
# answer is 188