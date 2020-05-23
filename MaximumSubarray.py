"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.


"""
class Solution: # NlogN
    def calc_cross_sum(self, nums, mid, left, right):
        
        if left == right:
            return nums[left]
            
        left_max = float('-inf')
        right_max = float('-inf')
        curr = 0
        # think of [-2,1,-3,4,-1,2,1,-5,4], you must start from mid to both side!!!
        for i in range(mid, left - 1, -1):
            curr += nums[i] # note that for cross case, we must take array going from left subarray to right subarray
            left_max = max(curr, left_max)

        curr = 0

        for i in range(mid+1, right+1): # right needs to + 1
            curr += nums[i]
            right_max = max(curr, right_max)

        return left_max + right_max




    def calc_sum(self, nums: List[int], left: int, right: int) -> int:

        if right - left == 0:
            return nums[right]

        mid = (left + right) // 2
        
        left_max = self.calc_sum(nums, left, mid)
        right_max = self.calc_sum(nums, mid + 1, right)
        cross_max = self.calc_cross_sum(nums, mid, left, right)
        
        print(left_max, right_max, cross_max)
        print(mid, left,right)
        print("-----")
        return max(left_max, right_max, cross_max)


    def maxSubArray(self, nums: 'List[int]') -> 'int':
        return self.calc_sum(nums, 0, len(nums) - 1)

######### Solution 2 : DP ################################3
class Solution:
         
    def maxSubArray(self, nums: 'List[int]') -> 'int':
        
        
        f = [0] * len(nums) # dynamic programming array to record the max sum if include current index
        max_sum_seen = [0] * len(nums) # store the final solution
        
        f[0] = nums[0]
        max_sum_seen[0] = nums[0]
        
        for i in range(1, len(nums)):
            # 3 cases:
            #   * include current
            #   * not include current
            #   * start a new one from current
            # special case: [2,5,3,-100,3,100] we need to start new one from 3
            f[i] = max(nums[i], f[i - 1] + nums[i]) # max_sum before me + me (must include me)
            max_sum_seen[i] = max(f[i], nums[i], max_sum_seen[i - 1])

            return max_sum_seen[-1]
            
            