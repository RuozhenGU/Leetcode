
# Given a string s, find the length of the longest substring without repeating characters.

from collections import Counter

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == '':
            return 0
        dp = [1] * len(s)
        
        hash_map = Counter()
        hash_map[s[0]] = 0
        max_ans =  1
        for i in range(1, len(s)):
            if s[i] not in hash_map:
                hash_map[s[i]] = i
                dp[i] = dp[i-1]  + 1  
            else:
                prev_loc = hash_map[s[i]]
                if i - dp[i-1] > prev_loc: 
                    dp[i] = dp[i - 1] + 1
                else:
                    dp[i] = i - prev_loc
                hash_map[s[i]] = i
            max_ans = max(max_ans, dp[i])
                    
        return max_ans