
'''
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

'''


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # turn into set to allow O(1)
        nums_set = set(nums)
        ans, count = 0, 0
        for num in nums_set:
            
            if num-1 not in nums_set: # KEY STEP: O (1)
                count = 1
                next_num = num + 1
                
                while next_num in nums_set:
                    count += 1
                    next_num += 1
                
                ans = max(ans, count)
            else:
                continue
        return ans