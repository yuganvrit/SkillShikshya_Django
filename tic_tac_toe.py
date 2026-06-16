"""
Tic-Tac-Toe Board Validator & 2-Player Game
----------------------------------------------
Board is a 3x3 nested list, with each cell being "X", "O", or " " (empty).

check_winner(board) returns one of:
  "X Wins"
  "O Wins"
  "Draw"
  "Game Ongoing"
"""


def create_board():
    """Return a fresh empty 3x3 board (nested list of spaces)."""
    return [[" " for _ in range(3)] for _ in range(3)]


def display_board(board):
    """Print the board in a readable grid format."""
    print()
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < 2:
            print("---------")
    print()


def check_winner(board):
    """
    Check rows, columns, and both diagonals for a winner.
    Returns "X Wins", "O Wins", "Draw", or "Game Ongoing".
    """

    lines = []

    # Rows
    for row in board:
        lines.append(row)

    # Columns
    for col in range(3):
        column = [board[row][col] for row in range(3)]
        lines.append(column)

    # Diagonals
    diagonal1 = [board[i][i] for i in range(3)]
    diagonal2 = [board[i][2 - i] for i in range(3)]
    lines.append(diagonal1)
    lines.append(diagonal2)

    # Check each line (row/column/diagonal) for three matching non-empty cells
    for line in lines:
        if line[0] != " " and line[0] == line[1] == line[2]:
            if line[0] == "X":
                return "X Wins"
            else:
                return "O Wins"

    # No winner yet -- check if the board is full (Draw) or has empty cells (Ongoing)
    for row in board:
        for cell in row:
            if cell == " ":
                return "Game Ongoing"

    return "Draw"


def get_move(player, board):
    """Ask the current player for a row and column, validating the input."""
    while True:
        try:
            raw = input(f"Player {player}, enter your move as 'row col' (0-2 0-2): ").strip()
            row_str, col_str = raw.split()
            row, col = int(row_str), int(col_str)
        except ValueError:
            print("Invalid input. Please enter two numbers separated by a space, e.g. '1 2'.\n")
            continue

        if not (0 <= row <= 2 and 0 <= col <= 2):
            print("Row and column must each be between 0 and 2.\n")
            continue

        if board[row][col] != " ":
            print("That cell is already taken. Choose another.\n")
            continue

        return row, col


def main():
    print("=== Tic-Tac-Toe ===")
    print("Players take turns. X goes first. Enter moves as 'row col' (0-2 0-2).\n")

    board = create_board()
    current_player = "X"

    while True:
        display_board(board)

        row, col = get_move(current_player, board)
        board[row][col] = current_player

        result = check_winner(board)

        if result != "Game Ongoing":
            display_board(board)
            if result == "Draw":
                print("It's a draw!")
            else:
                print(result + "!")
            break

        # Switch turns
        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    main()
