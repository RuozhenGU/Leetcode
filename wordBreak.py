"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words. You may assume the dictionary does not contain duplicate words.

For example, given
s = "leetcode",
dict = ["leet", "code"].
"""

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        _mem = {}
        
        if s == "": return False
        
        def search(s, wordDict):
            nonlocal _mem
            if s in _mem:
                return _mem[s]
            
            if s in wordDict:
                _mem[s] = True
                return True
            
            for i in range(1, len(s)):
                left_part = s[:i]
                right_part = s[i:]
                
                if left_part in wordDict:
                    
                    ans = search(right_part, wordDict)
                    _mem[right_part] = ans
                    
                    if ans:
                        return ans
            _mem[s] = False
            return False
        
        
        ans = search(s, set(wordDict))
        return ans