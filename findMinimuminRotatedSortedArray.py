
"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.
"""



class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l, r = 0, len(nums)
        
        if len(nums) == 1:  # super important
            return nums[0]
        
        if nums[0] < nums[-1]: # super important
            return nums[0]
        
        def binary_search_modified(l, r):
            nonlocal nums
            
            while l <= r:
                
                mid = (l + r) // 2
                print('curr', mid, l, r)
                
                if len(nums) == 1:
                    return nums[0]
                if mid + 1 < r:
                    if nums[mid] > nums[mid+1]: # [2,1] overflow
                        return mid+1
                    
                if mid - 1 >= 0: 
                    # very important, check front to prevent overflow
                    if nums[mid-1] > nums[mid]: 
                        return mid
               
                
                if nums[mid] < nums[0]:
                    r = mid - 1
                else:
                    l = mid + 1
                    
        return nums[binary_search_modified(l, r)] 