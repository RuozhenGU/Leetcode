'''
Consider a directed graph, with nodes labelled 0, 1, ..., n-1.  In this graph, each edge is either red or blue, and there could be self-edges or parallel edges.

Each [i, j] in red_edges denotes a red directed edge from node i to node j.  Similarly, each [i, j] in blue_edges denotes a blue directed edge from node i to node j.

Return an array answer of length n, where each answer[X] is the length of the shortest path from node 0 to node X such that the edge colors alternate along the path (or -1 if such a path doesn't exist).

Input: n = 3, red_edges = [[0,1],[1,2]], blue_edges = []
Output: [0,1,-1]

Input: n = 3, red_edges = [[0,1]], blue_edges = [[2,1]]
Output: [0,1,-1]

https://leetcode.com/problems/shortest-path-with-alternating-colors/discuss/339965/Python-BFS
'''


from collections import defaultdict, deque


class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        
        graph_red = defaultdict(list)
        graph_blue = defaultdict(list)
        copy_graph_red = defaultdict(list)
        copy_graph_blue = defaultdict(list)
        
        for x,y in red_edges:
            graph_red[x].append(y)
            copy_graph_red[x].append(y)
        
        for x,y in blue_edges:
            graph_blue[x].append(y)
            copy_graph_blue[x].append(y)
        
        red = -1
        blue = 1
        
        ans = [float('inf')] * n

        ##################################################################

        
        q = deque([(0, red, 0)]) # key step
                          
        while q:
            node, color, level = q.popleft()
            next_color = -1 * color
            
            graph = graph_red if color == red else graph_blue

            # record ans            
            ans[node] = min(ans[node], level)
            
            neighbours = graph[node][:]
            
            for nei in neighbours:
                # remove directly
                graph[node].remove(nei)
                q.append((nei, next_color, level+1))
                
        ##################################################################

        # repeat
        q = deque([(0, blue, 0)]) # key step
        graph_blue = copy_graph_blue
        graph_red = copy_graph_red
        level = -1
        while q:
            node, color, level = q.popleft()
            next_color = -1 * color
            
            graph = graph_red if color == red else graph_blue

            # record ans            
            ans[node] = min(ans[node], level)
            
            neighbours = graph[node][:]
            
            for nei in neighbours:
                # remove directly
                graph[node].remove(nei)
                q.append((nei, next_color, level+1))
                
        return [_ if _ != float('inf') else -1 for _ in ans]
                
            
       
            
                
            