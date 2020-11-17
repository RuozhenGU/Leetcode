# 1. create array using in order
# 2. binary search to assign mid value from array to curr root


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorder(self, root: TreeNode, stack: List[TreeNode]):
        if root:
            self.inorder(root.left, stack)
            stack.append(root)
            self.inorder(root.right, stack)

    def balanceBST_(self, root: TreeNode, stack, first: int, last: int):
        if first > last:
            return None
        mid = (first + last) // 2
        node = stack[mid]
        node.left = self.balanceBST_(node, stack, first, mid - 1)
        node.right = self.balanceBST_(node, stack, mid + 1, last)
        return node

    def balanceBST(self, root: TreeNode) -> TreeNode:
        stack = []
        self.inorder(root, stack)

        first = 0
        last = len(stack) - 1
        mid = (first + last) // 2
        balanceRoot = TreeNode(stack[mid].val, None, None)
        balanceRoot.left = self.balanceBST_(balanceRoot, stack, 0, mid - 1)
        balanceRoot.right = self.balanceBST_(balanceRoot, stack, mid + 1, last)
        return balanceRoot