def create_board():
    board
    return board


def print_board(board):



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

