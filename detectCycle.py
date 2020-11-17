from collections import defaultdict 
'''
To detect a back edge, keep track of vertices currently in the recursion stack of function for DFS traversal. 
If a vertex is reached that is already in the recursion stack, then there is a cycle in the tree. 
The edge that connects the current vertex to the vertex in the recursion stack is a back edge. 
Use recStack[] array to keep track of vertices in the recursion stack.
'''
class Graph(): 
    def __init__(self,vertices): 
        self.graph = defaultdict(list) 
        self.V = vertices 
  
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  
    def isCyclicUtil(self, v, visited, recStack): 
  
        # Mark current node as visited and  
        # adds to recursion stack 
        visited[v] = True
        recStack[v] = True
  
         
        for neighbour in self.graph[v]: 
            if visited[neighbour] == False: 
                if self.isCyclicUtil(neighbour, visited, recStack) == True:  # fucking important
                    return True
            elif recStack[neighbour] == True:  # fucking important
                return True
  
        
        recStack[v] = False  # fucking important
        return False
  
    # Returns true if graph is cyclic else false 
    def isCyclic(self): 
        visited = [False] * self.V 
        recStack = [False] * self.V 
        for node in range(self.V): 
            if visited[node] == False: 
                if self.isCyclicUtil(node,visited,recStack) == True: 
                    return True
        return False
  