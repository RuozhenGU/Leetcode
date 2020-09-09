
/*
For a binary tree T, we can define a flip operation as follows: choose any node, and swap the left and right child subtrees.

A binary tree X is flip equivalent to a binary tree Y if and only if we can make X equal to Y after some number of flip operations.

Given the roots of two binary trees root1 and root2, return true if the two trees are flip equivelent or false otherwise.
*/

/*
soln: only need to compare the children and see if children are same
soln2: revert to make sure for each node, left child is always smaller than right. then dfs to traverse 
*/

class Solution {
public:
    bool flipEquiv(TreeNode* root1, TreeNode* root2) {
        if (!root1 && !root2) {
            return true;
        } else if (!root1 || !root2) {
            return false;
        } else if (root1->val != root2->val) {
            return false;
        } else {
            return (flipEquiv(root1->left, root2->left) && flipEquiv(root1->right, root2->right)) || 
                    (flipEquiv(root1->left, root2->right) && flipEquiv(root1->right, root2->left));
        }

    }
};

// Time Complexity: O(min(N1,N2))