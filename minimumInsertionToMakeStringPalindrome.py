"""
Given a string s. In one step you can insert any character at any index of the string.

Return the minimum number of steps to make s palindrome.

A Palindrome String is one that reads the same backward as well as forward.


Input: s = "mbadm"
Output: 2
Explanation: String can be "mbdadbm" or "mdbabdm".
"""


def minInsertions(self, s: str) -> int:
    return len(s) - self.longestPalindromeSubseq(s)


# soluton from longestPalindromeSubseq


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
