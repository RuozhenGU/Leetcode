'''
Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6

The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6


'''

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        tmp = root
        def bt_to_ll(root):
            
            if root == None:
                return None
            
            # super important
            if root.left == None and root.right == None:
                return root
      
            left_tail = bt_to_ll(root.left)
        
            # this step is important to get prepared for next round
            right_furtherest = bt_to_ll(root.right)
            
            if left_tail:
                left_tail.right = root.right

                root.right = root.left # not left_tail
                root.left = None
            
            return right_furtherest if right_furtherest else left_tail
            
        bt_to_ll(root)
        return root