"""

Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
"""

from collections import deque 

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
    
        
        q = deque([root])

        node = None
        ans = []
        
        if root == None:
            return []

        while q:
            
            tmp = q
            q = deque() # think this like a ptr
            
            
            while tmp:
                node = tmp.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
            ans.append(node.val)
           
        return ans