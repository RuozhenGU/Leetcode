"""
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

其实就是给你一个array，让你算每个subarry的max值，subarray长度是k，每次后移一位。

下面算法借用deque 其中push pop leftright是 O（1）所以其实每个ele最后都visit 2次，runtime O（n）
"""


import collections


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        def clean_queue(q, idx):

            # remove first if not in window anymore
            if q and q[0] == i - k:
                q.popleft()

            while q and nums[q[-1]] < nums[i]:
                q.pop()

        if len(nums) * k == 0:
            return []
        if k == 1:
            return nums

        q = collections.deque()

        ans = [float("-inf")]

        for i, ele in enumerate(nums):
            if i <= k - 1:
                clean_queue(q, i)
                q.append(i)
                ans[0] = max(ans[0], nums[i])
            else:

                clean_queue(q, i)
                q.append(i)

                ans.append(nums[q[0]])
        return ans
