#!/usr/bin/python3
"""N queens interview question"""

import sys
"""Imported for argument retrival on the command line"""


def is_safe(board, row, col, N):
    """
    Check if it's safe to place a queen in the given position.

    Args:
        board (list[list[str]]): The current state of the chessboard.
        row (int): The row index to check.
        col (int): The column index to check.
        N (int): The size of the chessboard.

    Returns:
        bool: True if safe, False otherwise.
    """
    for i in range(row):
        if board[i][col] == 'Q':
            return False
        if col - (row - i) >= 0 and board[i][col - (row - i)] == 'Q':
            return False
        if col + (row - i) < N and board[i][col + (row - i)] == 'Q':
            return False
    return True

def solve_nqueens(N):
    """
    Main entry point for the N queens solver.

    Usage:
        nqueens N

    Args:
        N (int): The size of the chessboard.

    Prints:
        List of solutions (each solution as a list of tuples).
    """
    board = [['.' for _ in range(N)] for _ in range(N)]
    solutions = []

    def backtrack(row):
        """
        Solve the N queens problem using backtracking.

        Args:
            N (int): The size of the chessboard.

        Returns:
            list[list[tuple[int, int]]]: List of solutions, where each solution
                contains the row and column indices of queens.
        """
        if row == N:
            solutions.append([(i, board[i].index('Q')) for i in range(N)])
            return
        for col in range(N):
            if is_safe(board, row, col, N):
                board[row][col] = 'Q'
                backtrack(row + 1)
                board[row][col] = '.'

    backtrack(0)
    return solutions

def nqueens():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
        if N < 4:
            print("N must be at least 4")
            sys.exit(1)
        solutions = solve_nqueens(N)
        for solution in solutions:
            print([list(row) for row in solution])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    
if __name__ == "__main__":
    nqueens()