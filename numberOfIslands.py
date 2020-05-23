"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
"""

"""

Time complexity is O(M * N)
Every position will calculate 4 times(up, down, left, right) at least. Since there are m * n positions in the grid, the time complexity should be O(4 * m * n).

"""


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs(grid, head):
            """
            after visit, set cell to be 0
            """
            x, y = head
            print(x, y)

            if len(grid) == 0 or grid[x][y] != "1":
                return
            else:
                grid[x][y] = "0"
            
            if x - 1 >= 0 and grid[x - 1][y] == "1":
                dfs(grid, (x - 1, y))
            if x + 1 < len(grid) and grid[x + 1][y] == "1":
                dfs(grid, (x + 1, y))
            if y - 1 >= 0 and grid[x][y - 1] == '1':
                dfs(grid, (x, y - 1))
            if y + 1 < len(grid[0]) and grid[x][y + 1] == "1":
                dfs(grid, (x, y + 1))
        
        count = 0
        
        if len(grid) == 0:
            return count

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    count += 1
                    dfs(grid, (i, j))
                    
        return count 

            