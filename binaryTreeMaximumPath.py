"""
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in 
the tree along the parent-child connections. The path must contain at least one node and does not 
need to go through the root.

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
"""

"""
idea: max_sum(n) is max_sum(n->left) + max_sum(n->right) + n

if left and right is null, then max_sum of current node is 0

Run time: O(n)
space: O(logn)
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def maxPathSum(self, root):
    def maxPathSum(self, root : TreeNode) -> int:
        def calcPathSum(node):
            nonlocal max_sum_value
            if not node:
                return 0
            else:
                left_max_sum = calcPathSum(node.left)
                right_max_sum = calcPathSum(node.right)
                val = node.val

                curr_max_sum = max(val, (val + left_max_sum), (val + right_max_sum), (val + left_max_sum + right_max_sum))

                # update accumulator
                max_sum_value = max(curr_max_sum, max_sum_value)

                # first line is wrong! you cannot return curr_max_sum which means you wanna 
                #  include both childrens as max_sum. if you do so, you cannot make new path as
                #  we are recursing from the bottom of tree to top. you cannot make your parents
                #  link to this current max path. our above update accumulator step already considers
                #  if we do not have parents but just create a path using curr, its left and its right.
                return node.val + max(0, left_max_sum, right_max_sum)

        max_sum_value = root.val
        calcPathSum(root)
        return max_sum_value


