#!/usr/bin/python3
"""N queens interview question"""

import sys
"""Import the sys for getting the argument for the cli"""


def is_safe(board, row, col, N):
    """Check if a queen can be placed in the given position"""
    for i in range(row):
        if board[i][col] == 'Q':
            return False
        if col - (row - i) >= 0 and board[i][col - (row - i)] == 'Q':
            return False
        if col + (row - i) < N and board[i][col + (row - i)] == 'Q':
            return False
    return True

def solve_nqueens(N):
    """keeps track of all the positions"""
    board = [['.' for _ in range(N)] for _ in range(N)]
    solutions = []

    def backtrack(row):
        """backtrack through the board"""
        if row == N:
            solutions.append([''.join(row) for row in board])
            return
        for col in range(N):
            if is_safe(board, row, col, N):
                board[row][col] = 'Q'
                backtrack(row + 1)
                board[row][col] = '.'

    backtrack(0)
    return solutions

def main():
    """The main entry point"""
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
            for row in solution:
                print(row)
            print()
    except ValueError:
        print("N must be a number")
        sys.exit(1)

if __name__ == "__main__":
    main()