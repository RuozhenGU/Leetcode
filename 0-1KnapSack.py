"""
Given weights and values of n items, put these items in a knapsack of capacity W to get the 
maximum total value in the knapsack. In other words, given two integer arrays val[0..n-1] and wt[0..n-1] 
which represent values and weights associated with n items respectively. Also given an integer W which represents 
knapsack capacity, find out the maximum value subset of val[] such that sum of the weights of 
this subset is smaller than or equal to W.
"""

"""
at row i and column j (which represents the maximum value we can obtain there), 
we would pick either the maximum value that we can obtain without item i, 
or the maximum value that we can obtain with item i, whichever is larger.

step 1: fill in first row and col with 0
step 2: compute top to bottom: include or not include
"""

def knapSack(W: int, wt: list, val: list, n: int): 
    dp = [[0 for _ in range(W)] for _ in range(n)]

    for i in range(n):
        for j in range(W):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif wt[i] < W:
                include_benefit = val[i] + dp[i-1][W-wt[i]] # remaining 
                not_include_benefit = dp[i-1][j]

                dp[i][j] = max(include_benefit, not_include_benefit)
            else:
                # dont forget
                dp[i][j] = dp[i-1][j]
    return dp[n-1][W-1]


# test
val = [60, 100, 120] 
wt = [10, 20, 30] 
W = 50
n = len(val) 
print(knapSack(W, wt, val, n)) 