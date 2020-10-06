class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        # 2nd smallest element = 2th element in the inorder traversal
        def inorder(r):
            if r == None:
                return []
            else:
                return inorder(r.left) + [r.val] + inorder(r.right)

        return inorder(root)[k - 1]



class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = []
        
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if not k:
                return root.val
            root = root.right

            '''O(H+k), where HH is a tree height. 
            This complexity is defined by the stack, which contains at least H + kH+k elements, 
            since before starting to pop out one has to go down to a leaf. This results in \mathcal{O}(\log N + k)O(logN+k) for the balanced tree and \mathcal{O}(N + k)O(N+k) for completely unbalanced tree with all the nodes in the left subtree.
            '''