#!/usr/bin/python3
def pascal_triangle(n):
    '''
    This function represents Pascals triangle

    Args:
        n (int): The number of rows of the tirangle
    Returns:
        List of lists of integers representing Pascal's triangle
    '''

    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        if i == 0:
            triangle.append([1])
        else:
            row = [1]
            prev_row = triangle[i-1]
            for j in range(1, i):
                row.append(prev_row[j-1] + prev_row[j])
            row.append(1)
            triangle.append(row)
    return triangle
