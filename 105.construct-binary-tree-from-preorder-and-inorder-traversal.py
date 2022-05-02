#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def recur(preorder, inorder):
            if not preorder:
                return None
            rootVal = preorder.pop(0)
            root = TreeNode(rootVal)
            
            left_inorder = []
            left_preorder = []
            while inorder and inorder[0] != rootVal:
                left_inorder.append(inorder.pop(0))
                left_preorder.append(preorder.pop(0))
            inorder.pop(0)
            left = recur(left_preorder, left_inorder)
            right = recur(preorder, inorder)
            root.left = left
            root.right = right
            return root
        return recur(preorder, inorder)




            
# @lc code=end

