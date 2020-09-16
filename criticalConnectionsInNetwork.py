
"""There are n servers numbered from 0 to n-1 connected by undirected server-to-server connections forming a network where connections[i] = [a, b] represents a connection between servers a and b. Any server can reach any other server directly or indirectly through the network.

A critical connection is a connection that, if removed, will make some server unable to reach some other server.

Return all critical connections in the network in any order.
"""


# Strong connected component
from collections import defaultdict

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        
        graph = defaultdict(list)
        
        for i, j in connections:
            graph[i].append(j)
            graph[j].append(i)
        
        low = {} 
        ans = []
        
        def dfs(node, rank, parent): # important to pass parent
            nonlocal graph, low, ans
            
            # if node is in low
            if node not in low:
                low[node] = rank
                for nei in graph[node]:
                    if nei != parent: # we dont use visited to track!
                        actual = dfs(nei, rank + 1, node)
                        # check if expect == rank + 1
                        if actual >= rank + 1:
                            ans.append([node, nei])
                        
                        # nodes in cycle all have the same rank
                                        # not rank!!!
                        low[node] = min(low[node], actual)
                        
            return low[node]

        # main
        dfs(connections[0][0], 0, -1)

        return ans
                
        
        
        