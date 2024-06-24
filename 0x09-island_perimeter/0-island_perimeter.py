#!/usr/bin/python3
"""Interview question island perimeter"""

def island_perimeter(grid):
    """
        A function that returns the perimeter of the island described in grid

        grid is a list of list of integers:

            0 represents water
            1 represents land
            Each cell is square, with a side length of 1
            Cells are connected horizontally/vertically (not diagonally).
            grid is rectangular, with its width and height not exceeding 100
            The grid is completely surrounded by water
            There is only one island (or nothing).

        The island doesn’t have “lakes” (water that isn’t connected to the sea).
    """
    perimeter = 0

    if not grid:
        return perimeter

    rows, cols = len(grid), len(grid[0])

    for r in range(rows):
        for c in range(cols):
                if grid[r][c] == 1:
                    perimeter += 4
                    if c > 0 and grid[r][c - 1] == 1:
                         perimeter -= 2
                    if r > 0 and grid[r - 1][c] == 1:
                         perimeter -= 2

    return perimeter