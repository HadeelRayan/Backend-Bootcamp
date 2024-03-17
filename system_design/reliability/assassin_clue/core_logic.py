import random


def play_round(self):
    # Simulate player movements and actions
    for player in self.players:
        player.visit_places(self.places)
        print(f"{player.name} moves to {', '.join(player.visited_places)}.")

    # Assassin commits a murder
    murder_place = random.choice(self.places)
    print(f"A murder has happened at {murder_place} with {self.murder_weapon}.")


def get_player_input(self, prompt, valid_responses=None):
    while True:
        response = input(prompt).strip()
        if valid_responses is None or response in valid_responses:
            return response
        print("Invalid input, please try again.")


def player_actions(self):
    # Example player action phase
    for player in self.players:
        if player.is_assassin:
            continue  # Skip assassin for certain actions
        action = self.get_player_input(f"{player.name}, do you want to 'move' or 'accuse'? ", ['move', 'accuse'])
        if action == 'move':
            # Implement move logic
            pass
        elif action == 'accuse':
            accused = self.get_player_input("Who do you accuse? ", [p.name for p in self.players if p != player])
            if self.accuse_player(player, accused):
                return True  # Correct accusation
    return False
