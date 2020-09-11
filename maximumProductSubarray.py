class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        '''

        问题的核心是负数。两个负数相遇可以完全颠覆list

        解决方法是用another var to track min so far值。

        在每次compute max so far的时候，也考虑进去min so far * curr的结果。

        在每次update min so far的时候，也要考虑进去max so far * curr 【反例：【-1 -2 -9】】

        简单一句话，记住，一旦遇到一个负数，max 可以立刻变min，min也可以立刻变max。互相dependent，互相update
        '''
        if len(nums) == 0:
            return 0
        
        ans = nums[0] # very important, track final answer
        max_so_far = nums[0]
        min_so_far = nums[0]

        for i in range(1, len(nums)):
            curr = nums[i]
            tmp_min = min(min_so_far * curr, curr, max_so_far * curr)
            max_so_far = max(min_so_far * curr, curr, max_so_far * curr)
            
            min_so_far = tmp_min # must update later
            
            # if current max is larger than previous found max
            ans = max(ans, max_so_far)

        return ans

# -2 3 2 -4

10
20
