from copy import deepcopy

# Define spells
SPELLS = {
    "Magic Missile": {"cost": 53, "damage": 4, "heal": 0, "effect": None},
    "Drain": {"cost": 73, "damage": 2, "heal": 2, "effect": None},
    "Shield": {"cost": 113, "damage": 0, "heal": 0, "effect": {"armor": 7, "turns": 6}},
    "Poison": {"cost": 173, "damage": 0, "heal": 0, "effect": {"damage": 3, "turns": 6}},
    "Recharge": {"cost": 229, "damage": 0, "heal": 0, "effect": {"mana": 101, "turns": 5}},
}

# Initial player and boss stats
PLAYER_HP = 50
PLAYER_MANA = 500
BOSS_HP = 51
BOSS_DAMAGE = 9

# Apply effects
def apply_effects(player, boss, effects):
    player["armor"] = 0  # Reset armor to 0 before applying effects
    for effect, timer in effects.items():
        if timer > 0:
            if effect == "Shield":
                player["armor"] = SPELLS["Shield"]["effect"]["armor"]
            elif effect == "Poison":
                boss["hp"] -= SPELLS["Poison"]["effect"]["damage"]
            elif effect == "Recharge":
                player["mana"] += SPELLS["Recharge"]["effect"]["mana"]
            effects[effect] -= 1  # Decrease effect timer

# Simulate the game
def simulate(player, boss, effects, mana_spent, min_mana):
    # Base case: check for win/loss
    if boss["hp"] <= 0:
        return mana_spent  # Player wins
    if player["hp"] <= 0 or mana_spent >= min_mana:
        return float("inf")  # Player loses or spent too much mana

    # Apply effects at the start of the turn
    apply_effects(player, boss, effects)

    # Check again if the boss is dead after effects
    if boss["hp"] <= 0:
        return mana_spent

    # Try all spells
    for spell, properties in SPELLS.items():
        # Skip if not enough mana or if effect is active
        if properties["cost"] > player["mana"] or (properties["effect"] and effects.get(spell, 0) > 0):
            continue

        # Copy state
        new_player = deepcopy(player)
        new_boss = deepcopy(boss)
        new_effects = deepcopy(effects)

        # Cast the spell
        new_player["mana"] -= properties["cost"]
        new_mana_spent = mana_spent + properties["cost"]

        # Apply instant effects
        if spell == "Magic Missile":
            new_boss["hp"] -= properties["damage"]
        elif spell == "Drain":
            new_boss["hp"] -= properties["damage"]
            new_player["hp"] += properties["heal"]
        elif spell in ["Shield", "Poison", "Recharge"]:
            new_effects[spell] = SPELLS[spell]["effect"]["turns"]

        # Boss turn
        apply_effects(new_player, new_boss, new_effects)
        if new_boss["hp"] <= 0:
            return new_mana_spent  # Boss dies after effects

        # Boss attacks
        damage = max(1, BOSS_DAMAGE - new_player["armor"])
        new_player["hp"] -= damage

        # Recurse
        min_mana = min(min_mana, simulate(new_player, new_boss, new_effects, new_mana_spent, min_mana))

    return min_mana

# Run simulation
player = {"hp": PLAYER_HP, "mana": PLAYER_MANA, "armor": 0}
boss = {"hp": BOSS_HP}
effects = {spell: 0 for spell in SPELLS if SPELLS[spell]["effect"]}
min_mana_spent = simulate(player, boss, effects, 0, float("inf"))

print("Least mana spent to win:", min_mana_spent)
# answer is 900