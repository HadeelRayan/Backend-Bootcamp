import BoardCon


def initial_cinfiguration(board):
    """
    This function prompts the user to enter the coordinates of living cells on the board
    the user specifies these coordinates in the format 'row,col'
    after setting the initial living cells, the user is prompted to enter the number of rounds they wish to simulate.

    Parameters:
    - board (List[List[int]]): A 2D list representing the game board, where each element is either 0 (dead cell) or 1 (living cell).

    Returns:
    - Tuple[List[List[int]], int]: A tuple containing the configured board and the number of simulation rounds, as specified by the user.
    """

    print("Enter the coordinates of living cells in the format 'row,col' (e.g., 1,2). Type 'done' when finished:")

    while True:
        user_input = input("> ").strip()  # Get user input
        if user_input.lower() == 'done':
            break  # Exit loop if user is done entering cells

        try:
            row, col = map(int, user_input.split(','))  # Try to parse the coordinates
            if 0 <= row < len(board) and 0 <= col < len(board[0]):
                board[row][col] = 1  # Mark the cell as alive
            else:
                print("Error: Coordinates out of bounds. Please enter valid coordinates.")
        except ValueError:
            print("Error: Invalid input format. Please enter the coordinates in the format 'row,col'.")
    rounds = int(input("Enter the number of rounds you wish to simulate: "))
    print("The initial board state")
    BoardCon.print_board(board)
    return board, rounds
