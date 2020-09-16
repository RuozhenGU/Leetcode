"""
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Input:nums = [1,1,1], k = 2
Output: 2
"""

from collections import Counter
class Solution:
  
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        counter = Counter()
        counter[0] = 1
        sum_acc, ans = 0, 0
        
        for i, item in enumerate(nums):
            
            sum_acc = sum_acc + nums[i]
            if sum_acc - k in counter:
                ans += counter[sum_acc - k]
            
            counter[sum_acc] += 1
            
        return ans