"""
A message containing letters from A-Z is being encoded to numbers using the following mapping:
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
"""

class Solution:
    def __init__(self):
        self.memo = {}

    def recursive_with_memo(self, index, s) -> int:
        # base case for index + 2.
        if index == len(s):
            return 1

        # If the string starts with a zero, it can't be decoded
        if s[index] == '0':
            return 0

        # base case for index + 1
        if index == len(s)-1:
            return 1

        # Memoization 
        if index in self.memo:
            return self.memo[index]

        ans = self.recursive_with_memo(index+1, s) \
                + (self.recursive_with_memo(index+2, s) if (int(s[index : index+2]) <= 26) else 0) 
                # consider 226 => 3 rather than 2, need to consider step for both 1 and 2

        # Save
        self.memo[index] = ans

        return ans

    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        return self.recursive_with_memo(0, s)