"""
Given an m x n matrix. If an element is 0, set its entire row and column to 0. Do it in-place.

Follow up:

    A straight forward solution using O(mn) space is probably a bad idea.
    A simple improvement uses O(m + n) space, but still not the best solution.
    Could you devise a constant space solution?
"""

"""

I think what Chen tries to do is to store information at the first element of each columns and rows. If a column contains a 0, 
it's first element will be 0. Same for rows. However, both first column and first row use matrix[0][0] which is problematic so she 
creates another variable for first column, col0.
"""


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_is_for_row = False
        zero_is_for_col = False

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):

                if matrix[i][j] == 0:
                    if i == 0:
                        zero_is_for_row = True
                    if j == 0:
                        zero_is_for_col = True

                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[0][j] == 0 and j != 0:
                    matrix[i][j] = 0
                if matrix[i][0] == 0 and i != 0:
                    matrix[i][j] = 0

        if zero_is_for_row:
            for col in range(0, len(matrix[0])):
                matrix[0][col] = 0

        if zero_is_for_col:
            for row in range(0, len(matrix)):
                matrix[row][0] = 0
