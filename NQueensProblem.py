def solve_n_queens(n):
    """
    Solves the N-Queens problem and returns all valid board configurations.
    """
    solutions = []
    # Create an empty NxN board filled with '.'
    board = [["."] * n for _ in range(n)]

    # Sets to track under-attack zones
    cols = set()
    pos_diag = set()  # Tracks positive diagonals (row + col)
    neg_diag = set()  # Tracks negative diagonals (row - col)

    def backtrack(row):
        # Base Case: If all queens are successfully placed
        if row == n:
            # Format the board state into strings and save it
            current_solution = ["".join(r) for r in board]
            solutions.append(current_solution)
            return

        for col in range(n):
            # Check if this square is under attack
            if col in cols or (row + col) in pos_diag or (row - col) in neg_diag:
                continue

            # Place the queen
            board[row][col] = "Q"
            cols.add(col)
            pos_diag.add(row + col)
            neg_diag.add(row - col)

            # Recurse to place the queen in the next row
            backtrack(row + 1)

            # Backtrack: Remove the queen and try the next column
            board[row][col] = "."
            cols.remove(col)
            pos_diag.remove(row + col)
            neg_diag.remove(row - col)

    # Start the backtracking process from the 0th row
    backtrack(0)
    return solutions


# --- Driver Code to Test the Implementation ---
if __name__ == "__main__":
    n = 6
    all_solutions = solve_n_queens(n)

    print(f"Total distinct solutions for {n}-Queens: {len(all_solutions)}\n")
    for i, sol in enumerate(all_solutions, 1):
        print(f"Solution {i}:")
        for row in sol:
            print(row)
        print()
