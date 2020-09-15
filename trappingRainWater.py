"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it is able to trap after raining.

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
"""

# two pass
class Solution:
    def trap(self, height: List[int]) -> int:
        
        if height == []:
            return 0
        
        dp_left_to_right = [float('-inf')] * len(height)
        dp_right_to_left = [float('-inf')] * len(height)
        
        dp_left_to_right[0] = height[0]
        dp_right_to_left[-1] = height[-1]
        
        for i in range(1, len(height)):
            dp_left_to_right[i] = max(dp_left_to_right[i-1], height[i])
        
        for i in range(len(height)-2, -1, -1):
            dp_right_to_left[i] = max(dp_right_to_left[i+1], height[i])            
        area = 0
        
        for i in range(0, len(dp_right_to_left)):
            area += min(dp_right_to_left[i], dp_left_to_right[i]) - height[i]
        
        return area

# two ptrs

class Solution:
    def trap(self, height: List[int]) -> int:
        
        if height == []: return 0
        
        area = 0
        l, r = 0, len(height) - 1
        max_l = height[l]
        max_r = height[r]
        while l < r:
            if max_l < max_r:
                if max_l > height[l]:
                    area += max_l - height[l]
                l += 1
                max_l = max(height[l], max_l)
            else:
                if max_r > height[r]:
                    area += max_r - height[r]
                r -= 1
                max_r = max(height[r], max_r)
                
        return area