'''
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.
Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"
'''

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        print(s)
        
        stack = []
        
        start = 0 # the start idx of first element in stack
        
        ans = 0
        
        for i in range(len(s)):
            
            if s[i] == "(":
                stack.append(i)
                continue
            
            if len(stack) == 0: # if () ) () in the middle, can restart, there is no way to get a ) when stack empty, so just start next from current idx. discard previous 
                start = i + 1 # if (()), start is not updated
                              # if (((), start is not updated to wait for ) 
            else:
                idx = stack.pop()
                if stack == []: # find perfect complex match
                    ans = max(ans,i - start + 1)
                else:
                    ans = max(ans, i - stack[-1])
        return ans