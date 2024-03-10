#!/usr/bin/python3
""" This module contains a function that creates a pascal triangle """


def pascal_triangle(n):
    """ this creates a pascal triangle of n rows """
    triangle = []

    # i is the outer iterator for each list of numbers
    # j is the inner iterator for each number in the list

    for i in range(n):
        # first we create a list of 1s that we can then manipulate
        # at when calculating the inner numbers
        row = [1] * (i + 1)
        # once we reach the 3rd row, we can start calculating the inner numbers
        if i >= 2:
            # specify a range that cuts across all numbers except the first and
            # last numbers in the list
            for j in range(1, i):
                # calculate the inner numbers by adding the numbers in the
                # previous row that are directly above them
                # this works because triangle is a list of lists
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        # append the row to the triangle list
        triangle.append(row)

    return triangle
