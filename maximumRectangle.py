"""
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Input:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
Output: 6
"""

def maximalRectangle(self, matrix: List[List[str]]) -> int:
        dp = [[0]* len(matrix[0]) for _ in range(len(matrix))]
        max_area = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '0':
                    continue
            
                # update width
                if j != 0:
                    dp[i][j] = dp[i][j-1] + 1
                else:
                    dp[i][j] = 1

                # compare area
                width = dp[i][j]
                for row in range(i, -1, -1):
                    width = min(width, dp[row][j])    
                    area = abs(i - row + 1) * width
                    max_area = max(area, max_area)

        return max_area



class Solution:

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0

        m = len(matrix)
        n = len(matrix[0])

        left = [0] * n # initialize left as the leftmost boundary possible
        right = [n] * n # initialize right as the rightmost boundary possible
        height = [0] * n

        maxarea = 0

        for i in range(m):

            cur_left, cur_right = 0, n
            # update height
            for j in range(n):
                if matrix[i][j] == '1': height[j] += 1
                else: height[j] = 0
            # update left
            for j in range(n):
                if matrix[i][j] == '1': left[j] = max(left[j], cur_left)
                else:
                    left[j] = 0
                    cur_left = j + 1
            # update right
            for j in range(n-1, -1, -1):
                if matrix[i][j] == '1': right[j] = min(right[j], cur_right)
                else:
                    right[j] = n
                    cur_right = j
            # update the area
            for j in range(n):
                maxarea = max(maxarea, height[j] * (right[j] - left[j]))

        return maxarea