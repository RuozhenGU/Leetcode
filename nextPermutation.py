
"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

"""




from queue import PriorityQueue
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # 一定要观察到其实在从右往左走的时候，已经是一种sort了，在确保右一定小于左，否则停
        # 找到target时候下一步就是找谁来replace。找到的值swap，swap后要看出来descending order
        # 依旧preserve。所以只需要reverse一下target右侧
        
        i = len(nums) - 1
        while i >= 0:
            if i == 0:
                # if all descending ordered, then no next permutation
                for i in range(0, (len(nums)+1) // 2):
                    nums[i], nums[len(nums)-1-i] = nums[len(nums)-1-i], nums[i]
                return nums
            if nums[i-1] < nums[i]:
                i -= 1
                break
            i -= 1
        j = i + 1
        while j <= len(nums) - 2:
            if nums[i] < nums[j] and nums[i] >= nums[j+1]:
                break
            j += 1
            
        # swap
        nums[j], nums[i] = nums[i], nums[j]
        # reverse
        for m in range(0, (len(nums)-(i+1) + 1) // 2):
            l = m + i+1
            r = len(nums) - 1 - m
            nums[l], nums[r] = nums[r], nums[l]
        
        return nums
            