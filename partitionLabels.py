
"""
A string S of lowercase English letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.
"""


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last = {c: i for i, c in enumerate(S)}
        
        ans = []
        start = 0
        end = -1
        for i in range(len(S)):
            
            curr = S[i]
            last_pos = last[curr] + 1 # add1 important
            
            end = max(last_pos, end)
            
            if i == end-1:
                ans.append(S[start: end])
                start = end
                end = -1
                continue
                
        return map(len, ans)


"""
How about an approach using intervals. 
Compute interval (start, end) for each letter [a-z] , 
where start is first occurrence of letter, and end is last occurrence of letter. 
Then we merge any overlapping intervals, and the resulting intervals can form the answer.
"""