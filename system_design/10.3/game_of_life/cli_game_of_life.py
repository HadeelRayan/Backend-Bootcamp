import BoardCon
import UserCon


def get_neighbors(board, row, col):
    """Get the state (alive or dead) of all eight neighbors of a given cell."""
    neighbors = []
    for i in range(max(0, row - 1), min(row + 2, len(board))):
        for j in range(max(0, col - 1), min(col + 2, len(board[0]))):
            if (i, j) != (row, col):
                neighbors.append(board[i][j])
    return neighbors


def simulate_game_of_life(board, rounds):
    """Simulate the Game of Life for a given number of rounds."""
    for _ in range(rounds):
        print("Current Board:")
        print_board(board)
        board = update_board(board)
    print("Final Board after {} rounds:".format(rounds))
    print_board(board)
    return board


def main():
    game_board = create_board()
    initial_cinfiguration(game_board)
    game_simulation(game_board)


if __name__ == "__main__":
    main()
