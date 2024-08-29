#!/usr/bin/python3
'''implemeting island_perimeter function'''


def island_perimeter(grid):
    '''finds the island perimeter'''
    perimeter = 0

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] != 1:
                continue
            if row - 1 < 0 or grid[row - 1][col] == 0:
                perimeter += 1

            if row + 1 >= len(grid) or grid[row + 1][col] == 0:
                perimeter += 1

            if col - 1 < 0 or grid[row][col - 1] == 0:
                perimeter += 1

            if col + 1 >= len(grid[row]) or grid[row][col + 1] == 0:
                perimeter += 1

    return perimeter
