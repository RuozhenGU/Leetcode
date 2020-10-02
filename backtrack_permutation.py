class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums, tmp, ans):
            
            if len(tmp) == len(nums):
                ans.append(tmp[:])

            for i in range(0, len(nums)): # START FROM 0
                if nums[i] in tmp: # IMPORTANT SKIP
                    continue
                tmp.append(nums[i])
                backtrack(nums, tmp, ans)
                tmp.pop()

        ans = []

        tmp = []

        backtrack(nums, tmp, ans)

        return ans