
from collections import defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        # construct graph
        graph = defaultdict(set)
        for i, equa in enumerate(equations):
            x, y = equa
            graph[x].add((y, values[i]))
            graph[y].add((x, 1. / values[i]))
        
        print(graph)

        def dfs(start, end, visited,v ):
            nonlocal graph
            
            print("start", start)
            if start == end:
                return v

            visited.append(start)

            for neighbour, weight in graph[start]:
                if neighbour not in visited:
                    result = dfs(neighbour, end, visited, v * weight) # save temporarily
                    if result != -1: # important
                        return result
            return -1
        
        ans= []
        for query in queries:
            start, end = query
            if start not in graph or end not in graph:
                ans.append(-1)
            elif start == end:
                ans.append(1)
            else:
                visited = [start]
                v = 1
                ans.append(dfs(start, end, visited, v))
        return ans


        