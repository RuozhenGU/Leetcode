class Solution:
    def kSum(nums: List[int], target: int, k: int) -> List[List[int]]:
        nums.sort()
        res = []

        # Check if the sum of k smallest values is greater than target, or the sum of k largest values is smaller than target
        # if so, no need to continue, no such k sum exist
        if len(nums) == 0 or nums[0] * k > target or target > nums[-1] * k:
            return res
        if k == 2:
            return twoSum(nums, target)
        for i in range(len(nums)):
            if i == 0 or nums[i - 1] != nums[i]:
                for _, set in enumerate(kSum(nums[i + 1:], target - nums[i], k - 1)):
                    res.append([nums[i]] + set)
        return res

    def twoSum(nums: List[int], target: int) -> List[List[int]]:
        res = []
        lo, hi = 0, len(nums) - 1
        while (lo < hi):
            sum = nums[lo] + nums[hi]
            if sum < target or (lo > 0 and nums[lo] == nums[lo - 1]):
                lo += 1
            elif sum > target or (hi < len(nums) - 1 and nums[hi] == nums[hi + 1]):
                hi -= 1
            else:
                res.append([nums[lo], nums[hi]])
                lo += 1
                hi -= 1
        return res

