import BoardCon as Board


def count_living_neighbors(board, row, col):
    """
    Count the number of living neighbors around a specific cell.

    Parameters:
    - board (List[List[int]]): The game board.
    - row (int): The row index of the cell.
    - col (int): The column index of the cell.

    Returns:
    - int: The number of living neighbors.
    """
    max_row, max_col = len(board), len(board[0])
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),           (0, 1),
                  (1, -1), (1, 0), (1, 1)]  # Define the relative positions of neighbors

    living_neighbors = 0
    for d_row, d_col in directions:
        n_row, n_col = row + d_row, col + d_col
        if 0 <= n_row < max_row and 0 <= n_col < max_col and board[n_row][n_col] == 1:
            living_neighbors += 1

    return living_neighbors


def simulate_game_round(board):
    """
    Simulate one round of the Game of Life.

    Parameters:
    - board (List[List[int]]): The current state of the game board.

    Returns:
    - List[List[int]]: The state of the game board after one simulation round.
    """
    # Create a copy of the board to store the updates without affecting the original board during calculations
    new_board = [[0 for _ in row] for row in board]

    for row in range(len(board)):
        for col in range(len(board[row])):
            # Count living neighbors for the current cell
            living_neighbors = count_living_neighbors(board, row, col)

            # Apply the Game of Life rules based on the number of living neighbors
            if board[row][col] == 1:  # Rules for live cells
                if living_neighbors in [2, 3]:
                    new_board[row][col] = 1  # Cell remains alive
                else:
                    new_board[row][col] = 0  # Cell dies
            else:  # Rules for dead cells
                if living_neighbors == 3:
                    new_board[row][col] = 1  # Cell becomes alive

    return new_board


def simulate_game(board, rounds):
    """
    Simulate the Game of Life for a specified number of rounds.

    Parameters:
    - board (List[List[int]]): The initial state of the game board.
    - rounds (int): The number of rounds to simulate.

    Returns:
    - List[List[int]]: The state of the game board after all rounds have been simulated.
    """
    for i in range(rounds):
        board = simulate_game_round(board)
        print("Simulating round", {i+1}, ", this is the current game board ")
        Board.print_board(board)
    print("End of the game")
    return board
