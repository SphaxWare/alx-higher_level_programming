#!/usr/bin/python3
"""
Solves the N-queens puzzle.

Determines all possible solutions for
placing N non-attacking queens on an NxN chessboard.

USAGE: nqueens N

N must be an integer greater than or equal to 4.

Attributes:
    chessboard (list): A list of lists representing the chessboard.
    solutions (list): A list of lists containing solutions.

Solutions are represented as
[[row, column], [row, column], [row, column], [row, column]]
where `row` and `column` represent the position of a queen on the chessboard.
"""

import sys


def initialize_chessboard(size):
    """Initialize an `size`x`size` sized chessboard with empty spaces."""
    chessboard = []
    [chessboard.append([' ' for _ in range(size)]) for _ in range(size)]
    return chessboard


def copy_chessboard(chessboard):
    """Return a deepcopy of a chessboard."""
    if isinstance(chessboard, list):
        return list(map(copy_chessboard, chessboard))
    return chessboard


def get_solution(chessboard):
    """Return the list of lists representation of a solved chessboard."""
    solution = []
    for row in range(len(chessboard)):
        for col in range(len(chessboard)):
            if chessboard[row][col] == "Q":
                solution.append([row, col])
                break
    return solution


def mark_unavailable_positions(chessboard, row, col):
    """Mark positions on the chessboard
    where queens can no longer be placed."""
    for c in range(col + 1, len(chessboard)):
        chessboard[row][c] = "x"  # Mark forward positions
    for c in range(col - 1, -1, -1):
        chessboard[row][c] = "x"  # Mark backward positions
    for r in range(row + 1, len(chessboard)):
        chessboard[r][col] = "x"  # Mark positions below
    for r in range(row - 1, -1, -1):
        chessboard[r][col] = "x"  # Mark positions above

    # Mark positions diagonally down to the right
    c = col + 1
    for r in range(row + 1, len(chessboard)):
        if c >= len(chessboard):
            break
        chessboard[r][c] = "x"
        c += 1

    # Mark positions diagonally up to the left
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        chessboard[r][c] = "x"
        c -= 1

    # Mark positions diagonally up to the right
    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= len(chessboard):
            break
        chessboard[r][c] = "x"
        c += 1

    # Mark positions diagonally down to the left
    c = col - 1
    for r in range(row + 1, len(chessboard)):
        if c < 0:
            break
        chessboard[r][c] = "x"
        c -= 1


def recursive_solve(chessboard, current_row, placed_queens, solutions):
    """Recursively solve an N-queens puzzle.

    Args:
        chessboard (list): The current working chessboard.
        current_row (int): The current working row.
        placed_queens (int): The current number of placed queens.
        solutions (list): A list of lists of solutions.

    Returns:
        solutions
    """
    if placed_queens == len(chessboard):
        solutions.append(get_solution(chessboard))
        return solutions

    for col in range(len(chessboard)):
        if chessboard[current_row][col] == " ":
            temp_chessboard = copy_chessboard(chessboard)
            temp_chessboard[current_row][col] = "Q"
            mark_unavailable_positions(temp_chessboard, current_row, col)
            solutions = recursive_solve(
                temp_chessboard,
                current_row + 1,
                placed_queens + 1,
                solutions
            )
    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    chessboard = initialize_chessboard(int(sys.argv[1]))
    solutions = recursive_solve(chessboard, 0, 0, [])
    for solution in solutions:
        print(solution)
