#!/usr/bin/python3
"""
a function that returns the perimeter of the island
described in grid
"""


def island_perimeter(grid):
    """
    Returns the perimeter of the island
    Args:
            grid: a list of lists of integers
    Return:
            perimeter: the perimeter of the island described
    """
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])

    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1
                if j == cols - 1 or grid[i][j + 1] == 0:
                    perimeter += 1
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1
                if i == rows - 1 or grid[i + 1][j] == 0:
                    perimeter += 1
    return perimeter
