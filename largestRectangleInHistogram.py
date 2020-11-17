"""
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, 
find the area of largest rectangle in the histogram.

Input: [2,1,5,6,2,3]
Output: 10

https://leetcode.com/problems/largest-rectangle-in-histogram/
"""


# stack O(n) https://youtu.be/VNbkzsnllsU


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        # base case
        if heights == []:
            return 0

        hstack = []  # store height at this point
        pstack = []  # track starting index

        ans = float("-inf")

        temppos = 0
        size = 0
        i = 0

        # for loop gives error on [1, 1], equal height. because i - temppos = 0 - 0
        while i < len(heights):
            # current height at index i
            h = heights[i]
            # if stack is initially empty or its still in ascedningly order, keep pushing
            if len(hstack) == 0 or h >= hstack[len(hstack) - 1]:
                hstack.append(h)
                pstack.append(i)
            # find the ith height < i-1th height, start computing
            elif h < hstack[len(hstack) - 1]:
                # until find one on the left that is smaller than ith height
                while hstack and h < hstack[len(hstack) - 1]:
                    # at each pop, compute a height, try out all possible values till the leftmost
                    temph = hstack.pop()
                    temppos = pstack.pop()
                    size = temph * (i - temppos)
                    ans = max(size, ans)

                # okay, now ready to start over again from ith element, consider this is the new start
                hstack.append(h)
                pstack.append(temppos)
            i += 1

        while hstack:
            # repeat code
            temph = hstack.pop()
            temppos = pstack.pop()
            size = temph * (i - temppos)
            ans = max(size, ans)

        return ans


# time exceed solution: divide and conquer


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        def divide_conquer(heights, i, j):

            # print(i, j)

            if j == i:
                return 0

            if j - i == 1:
                return 1 * heights[i]

            smallest = min(heights[i:j])

            mid = heights[i:j].index(smallest) + i

            case1 = smallest * (j - i)

            case2 = divide_conquer(heights, i, mid)

            case3 = divide_conquer(heights, mid + 1, j)

            return max(case1, case2, case3)

        return divide_conquer(heights, 0, len(heights))