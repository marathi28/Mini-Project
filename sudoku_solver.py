# ============================================================
#   SUDOKU SOLVER USING RECURSION AND BACKTRACKING
#   Language  : Python 3.x
#   Algorithm : Backtracking with Recursion
#   Project   : CRT Mini Project — 2027 Batch
#   Dept      : Training & Placements
# ============================================================


def is_safe(board, row, col, num):
    """
    Check if placing 'num' at board[row][col] is valid.
    Validates the row, column, and the 3x3 sub-grid.
    """

    # Check if num already exists in the current row
    if num in board[row]:
        return False

    # Check if num already exists in the current column
    if num in [board[i][col] for i in range(9)]:
        return False

    # Check if num already exists in the 3x3 sub-grid
    start_row = 3 * (row // 3)
    start_col = 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True


def solve(board):
    """
    Solve the Sudoku puzzle using Recursion and Backtracking.
    Returns True if solved, False if no solution exists.
    """

    for row in range(9):
        for col in range(9):

            # Find an empty cell (represented by 0)
            if board[row][col] == 0:

                # Try placing digits 1 to 9
                for num in range(1, 10):
                    if is_safe(board, row, col, num):

                        # Place the digit
                        board[row][col] = num

                        # Recurse to solve the rest
                        if solve(board):
                            return True

                        # Backtrack — reset the cell
                        board[row][col] = 0

                # No valid digit found — trigger backtrack
                return False

    # All cells filled — puzzle solved
    return True


def print_board(board):
    """
    Display the Sudoku board in a formatted grid.
    Empty cells are shown as '.'
    """

    print("  + - - - + - - - + - - - +")
    for i, row in enumerate(board):
        if i % 3 == 0 and i != 0:
            print("  + - - - + - - - + - - - +")
        print("  |", end="")
        for j, val in enumerate(row):
            if j % 3 == 0 and j != 0:
                print(" |", end="")
            display = str(val) if val != 0 else "."
            print(f" {display}", end="")
        print(" |")
    print("  + - - - + - - - + - - - +")


def get_user_input():
    """
    Accept and validate the 9x9 Sudoku board from the user.
    Each row must have exactly 9 numbers between 0 and 9.
    0 represents an empty cell.
    """

    print("\n" + "=" * 45)
    print("       SUDOKU SOLVER — Enter Your Puzzle")
    print("=" * 45)
    print("  Enter each row as 9 space-separated digits.")
    print("  Use 0 for empty cells.  Example: 5 3 0 0 7 0 0 0 0")
    print("-" * 45)

    board = []
    for i in range(9):
        while True:
            try:
                row_input = input(f"  Row {i + 1}: ").strip().split()
                row = list(map(int, row_input))

                if len(row) != 9:
                    print("  ❌  Please enter exactly 9 numbers.")
                    continue

                if not all(0 <= x <= 9 for x in row):
                    print("  ❌  Each number must be between 0 and 9.")
                    continue

                board.append(row)
                break

            except ValueError:
                print("  ❌  Invalid input. Enter digits only (0–9).")

    return board


# ── Main Program ─────────────────────────────────────────────

def main():
    # Get puzzle input from user
    board = get_user_input()

    # Display the unsolved board
    print("\n  ─── Input Board ───")
    print_board(board)

    # Attempt to solve
    print("\n  Solving...")

    if solve(board):
        print("\n  ✔  Solved Successfully!\n")
        print("  ─── Solved Board ───")
        print_board(board)
    else:
        print("\n  ✘  No solution exists for the given puzzle.")

    print()


if __name__ == "__main__":
    main()
