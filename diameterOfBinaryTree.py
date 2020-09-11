"""
Given a binary tree, you need to compute the length of the diameter of the tree. 
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. 
This path may or may not pass through the root. 
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        
        if not root:
            return 0
        if not root.left and not root.right:
            return 0
        
        ans = 1
        
        def dfs(node):
            nonlocal ans
            if node == None:
                return 0
            else:
                left_max = dfs(node.left)
                right_max = dfs(node.right)
                ans = max(left_max + right_max, ans)  # important, we are not computing the depth!
                return max(left_max, right_max) + 1 # important for recursion update
        dfs(root)
        return ans


    