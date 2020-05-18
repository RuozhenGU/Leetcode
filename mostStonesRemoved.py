
import collections


def build_graph(stones):
    graph = collections.defaultdict(list)
    for i, stone in enumerate(stones):
        row, col = stone
        for j, other_stone in enumerate(stones):
            row2, col2 = other_stone
            if i != j and (row2 == row or col == col2):
                graph[i].append(j)
    return graph

def removeStones(self, stones: List[List[int]]) -> int:
    graph = build_graph(stones)
    visited = [False] * len(graph)
    max_steps = 0
    def dfs(v, graph, visited, curr_step):
        nonlocal max_steps
        visited[v] = True
        for neighbour in graph[v]:
            if not visited[neighbour]:
                curr_step += 1
                max_steps = max(max_steps, curr_step)
                dfs(neighbour, visited, curr_step)
    
    dfs(graph[0], graph, visited, 0)

    return max_steps
