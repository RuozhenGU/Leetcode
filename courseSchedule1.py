import collections

class Solution:
    
    WHITE, GRAY, BLACK = 0, 1, 2
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = collections.defaultdict(list)
        
        status = [0]*numCourses
        
        cycle = False
        
        for i, j in prerequisites:
            graph[i].append(j)
            # graph[j].append(i) must not have
            
        def dfs(node):
            nonlocal graph, status, cycle
            
            if cycle:
                return
            
            if status[node] == Solution.GRAY:
                return 
            
            status[node] = Solution.GRAY
            for nei in graph[node]:
                
                if status[nei] == Solution.WHITE:
                    dfs(nei)
                elif status[nei] == Solution.GRAY:
                    cycle = True # cycle
            
            status[node] = Solution.BLACK
            
        
        for i in range(len(status)):
            if status[i] == Solution.WHITE:
                dfs(i)
                
        if cycle:
            return False
        
        for item in status:
            if item == Solution.WHITE or item == Solution.GRAY:
                return False
        
        return True
            