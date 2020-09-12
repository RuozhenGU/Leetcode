"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia:

 “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants
  (where we allow a node to be a descendant of itself).”
"""

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        arr1 = []
        arr2 = []
        
        def traverse(root, arr, target):
            
            if root == None:
                return 0 # indicate false
            if root.val == target.val:
                arr.append(root)   # important if p is q's parent
                return 1
            arr.append(root)
            left = root.left
            right = root.right
            
            if left == None and right == None:  # important, need, it is and not or!
                return 0
            
            for node in [left, right]:
                if node == None:
                    continue
                r = traverse(node, arr, target)
                if r == 0:
                    arr.pop()
                    
                else:
                    return 1       # important
            return 0               # important
        
        traverse(root, arr1, p)
        traverse(root, arr2, q)
        for ele in arr1[::-1]:
            
            if ele in arr2:
                return ele
################### easier

class Solution {
public:
     TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if(root==NULL)
            return nullptr;
        if(p==root || q==root)
            return root;
        
        TreeNode*left = lowestCommonAncestor(root->left,p,q);
        TreeNode*right= lowestCommonAncestor(root->right,p,q);
        
        if(left != NULL && right != NULL)
            return root;
        if(left== NULL && right == NULL)
            return NULL;
        
        return left!=NULL ?left : right;
    }
};