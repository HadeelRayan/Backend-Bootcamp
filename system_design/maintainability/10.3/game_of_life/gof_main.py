import BoardCon
import UserCon
import GameSimulation


def main():
    game_board = BoardCon.create_board()
    game_board, rounds = UserCon.initial_cinfiguration(game_board)
    print("starting simulating the game")
    GameSimulation.simulate_game(game_board, rounds)


if __name__ == "__main__":
    main()
