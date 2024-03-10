

def get_neighbors(board, row, col):
    """Get the state (alive or dead) of all eight neighbors of a given cell."""
    neighbors = []
    for i in range(max(0, row - 1), min(row + 2, len(board))):
        for j in range(max(0, col - 1), min(col + 2, len(board[0]))):
            if (i, j) != (row, col):
                neighbors.append(board[i][j])
    return neighbors


def update_board(board):
    """Apply the Game of Life rules to the board and return the updated board."""
    new_board = create_board()  # Start with a new board to avoid modifying the input board in-place.
    for row in range(len(board)):
        for col in range(len(board[0])):
            alive_neighbors = sum(get_neighbors(board, row, col))
            if board[row][col] == 1:  # Cell is alive.
                # Apply underpopulation and overpopulation rules.
                if alive_neighbors < 2 or alive_neighbors > 3:
                    new_board[row][col] = 0
                else:
                    new_board[row][col] = 1
            else:  # Cell is dead.
                # Apply reproduction rule.
                if alive_neighbors == 3:
                    new_board[row][col] = 1
    return new_board


def simulate_game_of_life(board, rounds):
    """Simulate the Game of Life for a given number of rounds."""
    for _ in range(rounds):
        print("Current Board:")
        print_board(board)
        board = update_board(board)
    print("Final Board after {} rounds:".format(rounds))
    print_board(board)


def main():
    # Now, let's simulate the game with the previously initialized board and rounds.
    simulate_game_of_life(board, rounds)


if __name__ == "__main__":
    main()
