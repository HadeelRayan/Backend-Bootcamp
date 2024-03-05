import random
import itertools
import operator


class Player:
    def __init__(self, name):
        self.name = name
        self.ranking = random.randint(1500, 2000)
        self.points = 0

    def __repr__(self):
        return f"{self.name} (Ranking: {self.ranking}, Points: {self.points})"


def main():
    players = [Player(f"Player {i+1}") for i in range(4)]

    for i in range(len(players)):
        for j in range(i+1, len(players)):
            player1, player2 = players[i], players[j]

            total_ranking = player1.ranking + player2.ranking
            p1_win_prob = player1.ranking / total_ranking * 0.8
            p2_win_prob = player2.ranking / total_ranking * 0.8
            draw_prob = 0.2

            outcome = random.random()
            if outcome < draw_prob:
                player1.points += 0.5
                player2.points += 0.5
            elif outcome < draw_prob + p1_win_prob:
                player1.points += 1
            else:
                player2.points += 1

    winner = max(players, key=lambda x: x.points)
    print(winner)
    players_sorted_by_ranking = sorted(players, key=lambda x: x.ranking)
    print(players_sorted_by_ranking)
    players_sorted_by_points = sorted(players, key=lambda x: x.points, reverse=True)
    print(players_sorted_by_points)


if __name__ == "__main__":
    main()
