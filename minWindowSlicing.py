"""
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
"""

from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if s == "": return ""
        if len(s) < len(t): return ""
        
        l, r = 0, 1
        
        min_ans = float('inf')
        
        ans = ''
                
        target = Counter(t)
        
        missing = len(t)
        
        while r <= len(s):
            
            
            if s[r-1] in target and target[s[r-1]] > 0:
                if target[s[r-1]] != 0: # edge case bba and ab
                    missing -= 1

            target[s[r-1]] -= 1 # subtract for everything, irrelevant is saved as negative value
                
            if missing == 0:
                
                # move left ptr
                while l < r and target[s[l]] < 0: # fuck this shit!
                    
                    target[s[l]] += 1
                    l += 1
                    
                target[s[l]] += 1 # edge case bba and ab
                l += 1  # edge case bba and ab
                missing += 1        
                # save result
                if min_ans > r - (l-1):
                    min_ans = r - (l-1)
                    ans = s[(l-1): r]
                
            
            r += 1
        return ans