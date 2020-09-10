"""
problem:
Given a directed Eulerian graph, print an Euler circuit. Euler circuit is a path that traverses every edge of a graph, 
and the path ends on the starting vertex.

assume: such euler path must exist

algo:


Choose any starting vertex v, and follow a trail of edges from that vertex until returning to v. 
It is not possible to get stuck at any vertex other than v, because indegree and outdegree of every vertex must be same,
 when the trail enters another vertex w there must be an unused edge leaving w.

The tour formed in this way is a closed tour, but may not cover all the vertices and edges of the initial graph.
As long as there exists a vertex u that belongs to the current tour, but that has adjacent edges not part of the tour,
start another trail from u, following unused edges until returning to u, and join the tour formed in this way to the previous tour.

https://www.geeksforgeeks.org/hierholzers-algorithm-directed-graph/
"""

it

play_arrow

brightness_4
# Python3 program to print Eulerian circuit in given 
# directed graph using Hierholzer algorithm 
def printCircuit(adj): 
   
    # adj represents the adjacency list of 
    # the directed graph 
       
    if len(adj) == 0: 
        return # empty graph 
   
    # Maintain a stack to keep vertices 
    # We can start from any vertex, here we start with 0 
    curr_path = [0] 
   
    # list to store final circuit 
    circuit = [] 
   
    while curr_path: 
   
        curr_v = curr_path[-1] 
           
        # If there's remaining edge in adjacency list   
        # of the current vertex  
        if adj[curr_v]: 
  
            # Find and remove the next vertex that is   
            # adjacent to the current vertex 
            next_v = adj[curr_v].pop() 
   
            # Push the new vertex to the stack 
            curr_path.append(next_v) 
   
        # back-track to find remaining circuit 
        else: 
            # Remove the current vertex and  
            # put it in the curcuit 
            circuit.append(curr_path.pop()) 
   
    # we've got the circuit, now print it in reverse 
    for i in range(len(circuit) - 1, -1, -1): 
        print(circuit[i], end = "") 
        if i: 
            print(" -> ", end = "") 