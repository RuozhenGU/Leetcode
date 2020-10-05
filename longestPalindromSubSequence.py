"""
Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

Example 1:
Input:

"bbbab"

Output:

4
"""


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        dp = [[0] * len(s) for _ in range(len(s))]

        # init dp[i][i]
        for i in range(len(s)):
            dp[i][i] = 1

        # dp
        for i in range(len(s) - 1, -1, -1):  # IMPORTANT TO BE BOTTOM UP
            for j in range(i, len(s)):
                if j <= i:
                    continue
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])
        return dp[0][len(s) - 1]
