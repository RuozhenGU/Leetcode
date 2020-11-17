"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        d = [
            [1] * n for _ in range(m)
        ]  # , put number of paths equal to 1 for the first row and the first column.
        # means "takes 1 step to go to this cell"

        for row in range(m - 2, -1, -1):
            for col in range(n - 2, -1, -1):

                d[row][col] = d[row][col + 1] + d[row + 1][col]

        return d[0][0]