
def is_safe(board, row, col, num):
    if num in board[row]:
        return False
    if num in [board[i][col] for i in range(9)]:
        return False
    start_row = 3 * (row // 3)
    start_col = 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True

def is_valid_board(board):
    # Check rows
    for row in board:
        nums = [x for x in row if x != 0]
        if len(nums) != len(set(nums)):
            return False

    # Check columns
    for col in range(9):
        nums = []
        for row in range(9):
            if board[row][col] != 0:
                nums.append(board[row][col])

        if len(nums) != len(set(nums)):
            return False

    # Check 3x3 boxes
    for box_row in range(0, 9, 3):
        for box_col in range(0, 9, 3):
            nums = []

            for i in range(3):
                for j in range(3):
                    val = board[box_row + i][box_col + j]
                    if val != 0:
                        nums.append(val)

            if len(nums) != len(set(nums)):
                return False

    return True


def solve(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_safe(board, row, col, num):
                        board[row][col] = num
                        if solve(board):
                            return True
                        board[row][col] = 0
                return False
    return True


def print_board(board):
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

def main():
    
    board = get_user_input()

    if not is_valid_board(board):
        print("\n❌ Invalid Sudoku Puzzle!")
        return

    if solve(board):
        print("\n✔ Solved Successfully!")
        print_board(board)
    else:
        print("\n✘ No solution exists.")

if __name__ == "__main__":
    main()
