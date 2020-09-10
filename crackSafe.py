"""
There is a box protected by a password. The password is a sequence of n digits where each digit can be one of the first k digits 0, 1, ..., k-1.

While entering a password, the last n digits entered will automatically be matched against the correct password.

For example, assuming the correct password is "345", if you type "012345", the box will open because the correct password matches the suffix of the entered password.

Return any password of minimum length that is guaranteed to open the box at some point of entering it.

Input: n = 2, k = 2
Output: "00110"
Note: "01100", "10011", "11001" will be accepted too.
"""

"""
soln:

https://johnkyon.github.io/2018/08/30/leetcode753/

It's easy to take this problem as a graph theory, Let's take any number with n-1 digits as a vertex, to form a single and 
unique trial of the password, we extend a edge from this node, forming a n digits number. It also leads to the new node that
was indicated by it's [1:n] digits. So this problem is turned in to a graph problem defined as below:

Given a directed graph with kn−1
nodes, each nodes has k edges, pointed to another node. Find a path that visits every edges exactly once.
"""

class Solution:
    # with backtracking
    
     def crackSafe(self, n: int, k: int) -> str:
        
        ans = '0' * n
        
        def dfs(visited, n, k, total_len):
            nonlocal ans
            
            # base case: find euler path
            if total_len == len(ans): 
                return True 

            node = ans[len(ans) - (n - 1):] # last n - 1 nodes, not [1:]
            for x in map(str, range(k)): 
                
                node += x # construct new node
                
                if node not in visited: # if new node not visited
                    visited.add(node)
                    ans += x # important! construct the password by adding x into "shared previous built password"
                    if dfs(visited, n, k, total_len): # if going alone this path eventually will form Euler path 
                        return True
                    else:
                        visited.remove(node)
                        ans = ans[:-1]
                node = node[:-1] # very important
            return False
        
        visited = set()
        visited.add(ans) # super important !!!
        total_len = pow(k, n) + n - 1 # very important base case to check when to stop/obtain solution
        if dfs(visited, n, k, total_len):
            return ans
        else:
            return "" # unsolvable


# without backtracking

class Solution(object):
    def crackSafe(self, n, k):
        seen = set()
        ans = []
        def dfs(node):
            for x in map(str, range(k)):
                nei = node + x
                if nei not in seen:
                    seen.add(nei)
                    dfs(nei[1:])
                    ans.append(x)

        dfs("0" * (n-1))
        return "".join(ans) + "0" * (n-1)