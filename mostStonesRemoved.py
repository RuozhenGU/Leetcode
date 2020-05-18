'''
On a 2D plane, we place stones at some integer coordinate points.  Each coordinate point may have at most one stone.

Now, a move consists of removing a stone that shares a column or row with another stone on the grid.

What is the largest possible number of moves we can make to remove all stones?


Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
Output: 5

DFS: O(n^2)
'''


def removeStones(self, stones: List[List[int]]) -> int:
        def build_graph(stones):
            graph = {}
            for i, stone in enumerate(stones):
                graph[i] = []
                row, col = stone
                for j, other_stone in enumerate(stones):
                    row2, col2 = other_stone
                    if i != j and (row2 == row or col == col2):
                        graph[i].append(j)
            return graph
        
        def dfs(v, graph, visited):
            nonlocal max_steps
            nonlocal curr_step
            visited[v] = True
            for neighbour in graph[v]:
                if not visited[neighbour]:
                    curr_step += 1
                    dfs(neighbour, graph, visited)

        
        graph = build_graph(stones)
        visited = [False] * len(graph)
        max_steps = 0
        for key in graph.keys():
            if visited[key] == True:
                continue
            curr_step = 0
            dfs(key, graph, visited)
            max_steps += curr_step

        return max_steps