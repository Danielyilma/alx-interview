#!/usr/bin/python3
'''
implement a function that rotates 90 degree clockwise
'''

# def rotate_2d_matrix(matrix):
#     n = len(matrix)
#     rotated_matrix = []

#     for i in range(n):
#         temp = []
#         for j in range(n- 1, -1, -1):
#             temp.append(matrix[j][i])
#         rotated_matrix.append(temp)

#     for i in range(n):
#         for j in range(n):
#             matrix[i][j] = rotated_matrix[i][j]


def rotate_2d_matrix(matrix):
    '''rotating 2d matrix'''
    n = len(matrix)

    for i in range(n - 1):
        '''loop in over the cycle'''

        for j in range(i, n - 1 - i):
            '''looping over elements in one cycle'''

            # holding the top left column in the cycle
            temp = matrix[i][j]

            #  assigning bottom left to top left
            matrix[i][j] = matrix[n - 1 - j][i]

            # assigning bottom right to bottom left
            matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]

            # assigning top right to bottom right
            matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]

            # assigning top left to top right
            matrix[j][n - 1 - i] = temp
