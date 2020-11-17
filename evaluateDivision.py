
'''
You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

 

Example 1:

Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation: 
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
'''



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


        