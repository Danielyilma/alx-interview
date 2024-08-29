#!/usr/bin/python3
'''implemeting island_perimeter function'''


def island_perimeter(grid):
    '''finds the island perimeter'''
    perimeter = 0

    for row in range(1, len(grid) - 1):
        for col in range(1, len(grid[row]) - 1):
            if grid[row][col] != 1:
                continue
            if grid[row - 1][col] == 0:
                perimeter += 1

            if grid[row + 1][col] == 0:
                perimeter += 1

            if grid[row][col - 1] == 0:
                perimeter += 1

            if grid[row][col + 1] == 0:
                perimeter += 1

    return perimeter
