import random


class Pokemon:
    def __init__(self, name, level, strength, speed, pokemon_type):
        self.name = name
        self.level = level
        self.strength = strength
        self.speed = speed
        self.pokemon_type = pokemon_type
        self.life = 120

    def take_damage(self, damage):
        self.life -= damage
        if self.life <= 0:
            print(f"{self.name} has fainted!")
            return True
        return False

    def __str__(self):
        return self.name


def who_attacks_first(pokemon1, pokemon2):
    if (random.randint(1, 20) + pokemon1.speed) >= (random.randint(1, 20) + pokemon2.speed):
        attacker = pokemon1
    else:
        attacker = pokemon2
    return attacker


def determine_type_modifier(attacker_type, defender_type):
    types = {
        'fire': {'fire': 0.5, 'water': 2, 'earth': 1, 'wind': 2},
        'water': {'fire': 1, 'water': 0.5, 'earth': 2, 'wind': 1},
        'earth': {'fire': 2, 'water': 1, 'earth': 0.5, 'wind': 2},
        'wind': {'fire': 1, 'water': 2, 'earth': 1, 'wind': 0.5}
    }
    if defender_type in types[attacker_type]:
        return types[attacker_type][defender_type]
    else:
        return 1  # Default type modifier


def main():
    pokemons_player1 = [
        Pokemon("Kyogre", 2, 4, 3, 'fire'),
        Pokemon("Squirtle", 1, 7, 4, 'water'),
        Pokemon("Groudon", 1, 6, 2, 'earth'),
        Pokemon("Mewtwo", 1, 5, 5, 'wind'),
        Pokemon("Pikachu", 1, 9, 3, 'wind')
    ]

    pokemons_player2 = [
        Pokemon("Cyndaquil", 1, 8, 3, 'fire'),
        Pokemon("Totodile", 1, 7, 4, 'water'),
        Pokemon("Lugia", 1, 6, 2, 'earth'),
        Pokemon("Hoothoot", 1, 5, 5, 'wind'),
        Pokemon("Mareep", 1, 9, 3, 'wind')
    ]

    pokemon1 = random.choice(pokemons_player1)
    pokemon2 = random.choice(pokemons_player2)

    print(f"Player 1: {pokemon1.name}")
    print(f"Player 2: {pokemon2.name}")

    print("The Beginning")
    while True:
        attacker = who_attacks_first(pokemon1, pokemon2)
        defender = pokemon2 if attacker is pokemon1 else pokemon1

        damage = determine_type_modifier(attacker.pokemon_type, defender.pokemon_type) * (random.randint(1, 20) + attacker.strength)
        defender.life -= damage

        print(f"{attacker.name} attacks {defender.name}. Deals {damage} damage."
              f" {defender.name} now has {defender.life} amount of life after the attack.\n")

        if defender.life <= 0:
            print(f"{defender.name} is Dead")
            if pokemon1 == defender:
                pokemons_player1.remove(defender)
                if pokemons_player1:
                    pokemon1 = random.choice(pokemons_player1)
                    print(f"{pokemon1.name} has joined the fight!")
                else:
                    print("pokemon2 wins!")
                    break
            else:
                pokemons_player2.remove(defender)
                if pokemons_player2:
                    pokemon2 = random.choice(pokemons_player2)
                    print(f"{pokemon2.name} has joined the fight!")
                else:
                    print("pokemon1 wins!")
                    break

    print("The End")


if __name__ == "__main__":
    main()
