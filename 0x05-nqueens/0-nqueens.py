#!/usr/bin/python3
'''nqueens backtracking problem'''
import sys


def is_valid(solution, point):
    '''validating if a point can be placed(can not be attacked)'''
    for a_point in solution:
        if a_point[1] == point[1]:
            return False
        dis = abs(a_point[0] - point[0])
        if a_point[1] + dis == point[1] or point[1] + dis == a_point[1]:
            return False
    return True


def traverse(solution, row, n):
    '''find possible path for a row'''
    poss = []
    for col in range(n):
        if is_valid(solution, (row, col)):
            poss.append([row, col])
    return poss


def main(n):
    '''main excution'''
    result = []
    solution = []
    possible_path = [[0, i] for i in range(n)]
    row = 1

    while len(possible_path) > 0:
        solution.append(possible_path.pop())
        found_path = traverse(solution, row, n)

        if len(solution) == n:
            result.append(solution.copy())

        if found_path == [] or row >= n:
            if len(possible_path) > 0:
                temp = possible_path[-1]

            while solution[-1][0] != temp[0]:
                solution.pop()
            solution.pop()
            row = temp[0] + 1
            continue
        possible_path.extend(found_path)
        row += 1
    return (result)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    try:
        arg = int(sys.argv[1])
    except Exception as e:
        print("N must be a number")
        exit(1)

    if arg < 4:
        print("N must be at least 4")
        exit(1)

    for place in main(arg):
        print(place)
