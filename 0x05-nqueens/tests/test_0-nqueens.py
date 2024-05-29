import unittest
from nqueens import solve_nqueens  # Assuming your main code is in a file named "nqueens.py"

class TestNQueens(unittest.TestCase):
    def test_4_queens(self):
        # Test the solution for N = 4
        solutions = solve_nqueens(4)
        expected_solution = [
            [[0, 1], [1, 3], [2, 0], [3, 2]],
            [[0, 2], [1, 0], [2, 3], [3, 1]]
        ]
        self.assertEqual(solutions, expected_solution)

    def test_6_queens(self):
        # Test the solution for N = 6
        solutions = solve_nqueens(6)
        expected_solution = [
            [[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]],
            [[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]],
            [[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]],
            [[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
        ]
        self.assertEqual(solutions, expected_solution)

if __name__ == "__main__":
    unittest.main()