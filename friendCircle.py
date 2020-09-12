




class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        visited = []
        
        def dfs(i):
            nonlocal M, visited
            visited.append(i)
            for j in range(len(M)):
                if M[i][j] == 1 and j not in visited:
                    dfs(j)
        
        
        count = 0
        
        for i in range(len(M)):
                if i not in visited:
                    count += 1
                    dfs(i)
        return count