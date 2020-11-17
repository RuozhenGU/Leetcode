"""
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
"""

"""
Time Complexity: O(M^2×N), where M is the length of each word and N is the total number of words in the input word list.

note that substring takes O(N)

"""



import collections
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):

        if not wordList:
            return 0
        if endWord not in wordList or not endWord or not beginWord:
            return 0
        # construct graph
        graph = collections.defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                intermediate_word = word[:i] + "*" + word[i + 1:]
                graph[intermediate_word].append(word)
                
        # bfs 
        visited = {beginWord: True}
        queue = collections.deque([(beginWord, 1)]) # default a list, inside put tuple
        while queue:
            node, level = queue.popleft()
            for i in range(len(node)):
                intermediate_word = node[:i] + "*" + node[i + 1:]
                neighbours = graph[intermediate_word]
                for neighbour in neighbours:
                    if neighbour == endWord:
                        return level + 1
                    if not neighbour in visited:
                        visited[neighbour] = True
                        queue.append([neighbour, level + 1])
        return 0 # if reach here, no solution !!!!!!
        
        

