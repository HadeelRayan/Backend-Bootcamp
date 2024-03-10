def create_board(size=8):
    """
    Initialize an empty board for Game of Life.

    Parameters:
    - size (int): The width and height of the square board. Default is 8.

    Returns:
    - List[List[int]]: A 2D list representing the board, filled with 0s.
    """
    board = [[0 for _ in range(size)] for _ in range(size)]
    return board


def print_board(board):
    """
    Print the current state of the game board.

    Parameters:
    - board (List[List[int]]): The game board to print, where 0 represents a dead cell and 1 represents a living cell.
    """
    for row in board:
        print(' '.join(['▓' if cell == 1 else '░' for cell in row]))
    print()  # Add an extra newline for better readability between prints.


