"""
There is a new alien language which uses the latin alphabet. 
However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary,
 where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.

 Input:
[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]

Output: "wertf"
"""

# detect cycle + topological sort dfs


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        
        def dfs(node, visited, graph, stack, cycle):
            ans = True
            
            visited.append(node)
            cycle.append(node)
            for n in graph[node]:
                if n not in visited:
                    ans = dfs(n, visited, graph, stack, cycle)
                if n in cycle: # important
                    return False
                    
                if not ans:
                    return False
            cycle.remove(node) # important
            stack.append(node)
            return ans
    
    
        adj_list = {c : [] for word in words for c in word}

        # Step 1: Find all edges and put them in reverse_adj_list.
        for first_word, second_word in zip(words, words[1:]):
            for c, d in zip(first_word, second_word):
                if c != d: 
                    adj_list[d].append(c) # reversely!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                    break
            else: # Check that second word isn't a prefix of first word.
                if len(second_word) < len(first_word): 
                    return ""
                
        # Step 2: We need to repeatedly pick off nodes with an indegree of 0.
        stack = []
        visited = []
        cycle = []
        
        for key in list(adj_list):
            if key not in visited:
                if not dfs(key, visited, adj_list, stack, cycle):
                    return ""
                    
        # Otherwise, convert the ordering we found into a string and return it.
        ans = ''.join(stack)
        
        return ans
