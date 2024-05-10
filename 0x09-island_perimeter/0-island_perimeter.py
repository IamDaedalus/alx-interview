#!/usr/bin/python3
""" Island Perimeter Problem """


def island_perimeter(grid):
    """ calculates the island perimeter of the grid """
    perimeter = 0
    if type(grid) is not list:
        return 0

    rows, cols = len(grid), len(grid[0])

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                perimeter += 4
                if r > 0 and grid[r - 1][c] == 1:
                    perimeter -= 2
                if c > 0 and grid[r][c - 1] == 1:
                    perimeter -= 2

    return perimeter
