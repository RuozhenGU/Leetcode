
'''
Given an array nums of n integers where n > 1, 
 return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Input:  [1,2,3,4]
Output: [24,12,8,6]
'''


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        
        L, R, answer = [0]*length, [0]*length, [0]*length
    
        L[0] = 1
        for i in range(1, length):
            L[i] = nums[i - 1] * L[i - 1]
        
        R[length - 1] = 1
        for i in reversed(range(length - 1)):
            R[i] = nums[i + 1] * R[i + 1]
        
        # Constructing the answer array
        for i in range(length):
            answer[i] = L[i] * R[i]
        
        return answer

#O(n) + O(1) space
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        ans = [1] * len(nums)
        
        l_prod, r_prod = nums[0], nums[-1]
        for i in range(1, len(nums)):
            ans[i] = l_prod
            l_prod *= nums[i]
        for j in range(len(nums)-2, -1, -1):
            ans[j] *= r_prod
            r_prod *= nums[j]
        return ans