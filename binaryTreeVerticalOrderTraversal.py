from collections import defaultdict
'''
Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.


Input: [3,9,20,null,null,15,7]

   3
  /\
 /  \
 9  20
    /\
   /  \
  15   7 

Output:

[
  [9],
  [3,15],
  [20],
  [7]
]

'''

class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        column_ans = defaultdict(list)
        queue = [(root, 0)]

        range_col_min = 0
        range_col_max = 0

        while queue:
            node, col = queue.pop(
                0
            )  # MUST USE QUEUE, otherwise not vertical from left to right
            # eg: [[4],[9],[3,1,0],[8],[7]] instead of [[4],[9],[3,0,1],[8],[7]]

            if node:
                column_ans[col].append(node.val)  # only node.val, no left/right

                queue.append((node.left, col - 1))
                queue.append((node.right, col + 1))

                range_col_min = min(range_col_min, col)  # not -1
                range_col_max = max(range_col_max, col)  # not + 1

        return [column_ans[x] for x in range(range_col_min, range_col_max + 1)]
