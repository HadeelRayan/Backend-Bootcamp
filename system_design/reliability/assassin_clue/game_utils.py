import random
import player_utils as Player


class Game:
    def __init__(self, places, weapons, player_names):
        self.assassin = None
        self.places = places
        self.weapons = weapons
        self.players = [Player.Player(name) for name in player_names]
        self.murder_weapon = random.choice(self.players[0].favorite_weapons)  # Assassin's weapon

    def assign_assassin(self):
        assassin = random.choice(self.players)
        assassin.is_assassin = True
        self.assassin = assassin

    def assign_favorites(self):
        for player in self.players:
            player.favorite_weapons = random.sample(self.weapons, 2)

    def simulate_round(self):
        murder_place = random.choice(self.places)
        for player in self.players:
            player.visit_places(self.places)
            if player.is_assassin:
                print(f"\nA murder has happened at {murder_place} with {self.murder_weapon}!")
                player.visited_places.append(murder_place)  # Ensure assassin visits the murder place

    def accuse_player(self, accuser, accused_name):
        accused = next((player for player in self.players if player.name == accused_name), None)
        if accused and accused.is_assassin:
            print(f"{accuser.name} has correctly accused {accused_name}! Game over.")
            return True
        elif accused:
            print(f"{accuser.name} has wrongly accused {accused_name}. The game continues.")
            return False
        else:
            print("Invalid player name.")
            return False

    def get_valid_accusation(self, player):
        while True:
            accused_name = input(f"{player.name}, who do you accuse? ").strip()
            if self.accuse_player(player, accused_name):
                return True  # Correct accusation
            if accused_name in [p.name for p in self.players if p.name != player.name]:
                return False  # Wrong accusation but valid player

    def start(self):
        print("Game Starting\n")
        round_number = 1
        while len(self.players) > 1:
            print(f"\n Round {round_number}")
            self.simulate_round()

            for player in self.players:
                if player.is_assassin:
                    continue  # Assassin doesn't accuse
                if self.get_valid_accusation(player):
                    return  # Game ends with correct accusation

            round_number += 1

        print(f"Game over. The assassin {self.assassin.name} wins.")

