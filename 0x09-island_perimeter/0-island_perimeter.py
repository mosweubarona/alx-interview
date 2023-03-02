#!/usr/bin/python3
"""
This module contains the island_perimeter function which calculates
the perimeter of the island described in a grid.
"""


def island_perimeter(grid):
    """
    Calculates the perimeter of the island described in grid.

    Args:
    - grid: a list of list of integers representing an island n water

    Returns:
    - The perimeter of the island (an integer).

    Constraints:
    - The input grid is rectangular, with its width and height not >100.
    - The grid is completely surrounded by water.
    - There is only one island (or nothing).
    - The island doesn’t have “lakes” (water inside that isn’t connected.
    - Cells are connected horizontally/vertically (not diagonally).
    - Each cell is square, with a side length of 1.
    """

    # get the number of rows and columns in the grid
    rows = len(grid)
    cols = len(grid[0])

    # initialize the total perimeter to 0
    total_perimeter = 0

    # loop through each cell in the grid
    for r in range(rows):
        for c in range(cols):

            # if the cell contains a land, add 4 to the perimeter
            if grid[r][c] == 1:
                total_perimeter += 4

                # if the cell to the left also contains land, subtract 2
                if c > 0 and grid[r][c-1] == 1:
                    total_perimeter -= 2

                # if the cell above also contains land, subtract 2
                if r > 0 and grid[r-1][c] == 1:
                    total_perimeter -= 2

    # return the total perimeter
    return total_perimeter
