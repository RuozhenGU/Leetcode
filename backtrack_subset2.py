    """
    
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]

    """

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums, tmp, ans, start):

            ans.append(tmp[:])

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]: # SKIP duplicates
                    continue
                tmp.append(nums[i])
                backtrack(nums, tmp, ans, i + 1)
                tmp.pop()

        ans = []

        tmp = []

        nums.sort() # IMPORTANT

        backtrack(nums, tmp, ans, 0)

        return ans