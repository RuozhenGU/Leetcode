'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

'''
# Our complexity analysis rests on understanding how many elements there are in generateParenthesis(n). 
# This analysis is outside the scope of this article, but it turns out this is the n-th Catalan number 1n+1(2nn)\dfrac{1}{n+1}\binom{2n}{n}n+11​(n2n​), 
# which is bounded asymptotically by 4^n\dfrac{4^n}{n\sqrt{n}}nn

# https://leetcode.com/problems/generate-parentheses/solution/
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(left, right, total, str_so_far):
            
            if len(str_so_far) == 2 * total:
                ans.append(str_so_far)
            
            if left < total: # still can append (
                backtrack(left+1, right, total, str_so_far +"(" )
            if right < left: # append ) only when more ( then )
                backtrack(left, right+1, total, str_so_far +")" )
        
        
        
        if n == 1:
            return ["()"]
        else:
            backtrack(0, 0, n, "") # start with empty str
        return ans
