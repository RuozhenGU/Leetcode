"""

 Find all unique triplets in the array which gives the sum of zero.

 note: need to sort to skip the duplicate values!!!
 """

# important: after sort, consider duplicates

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]: # If the current value is the same as the one before, skip it.
                self.twoSumII(nums, i, res)
        return res

    def twoSumII(self, nums: List[int], i: int, res: List[List[int]]):
        lo, hi = i + 1, len(nums) - 1
        while (lo < hi):
            sum = nums[i] + nums[lo] + nums[hi]
            if sum < 0:
                lo += 1
            elif sum > 0:
                hi -= 1
            else:
                res.append([nums[i], nums[lo], nums[hi]]) # since we need to find all
                lo += 1
                hi -= 1
                # Increment lo while the next value is the same as before to avoid duplicates in the result.
                while lo < hi and nums[lo] == nums[lo - 1]: 
                    lo += 1