/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
//     bool isEqual(TreeNode* a, TreeNode* b){
//         if(!a && !b)
//             return true;
//         if((!a && b) || (a && !b) || !a->left && a->right || a->left && !a->right)
//             return false;
        
//         bool ans = a->left->val == a->right->val;
        
//         if(!a->left && !b->left )
//             return ans && isEqual(a->right, b->right);
//         if(!a->right && !b->right )
//             return ans && isEqual(a->left, b->left);
        
        
//         return ans && isEqual(a->left, b->left) && isEqual(a->right, b->right)  ;
        
//     }
    bool isEqual(TreeNode* a, TreeNode* b){
        if(!a && !b)
            return true;
        if(!a || !b)
            return false;
        return a->val==b->val && isEqual(a->left, b->right) && isEqual(a->right, b->left);
    }
    bool isSymmetric(TreeNode* root) {
        return isEqual(root->left, root->right);
        
        
        
    }
};