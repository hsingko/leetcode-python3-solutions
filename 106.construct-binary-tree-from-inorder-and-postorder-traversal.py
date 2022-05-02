#
# @lc app=leetcode id=106 lang=python3
#
# [106] Construct Binary Tree from Inorder and Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        def recur(inorder, postorder):
            if not inorder:
                return None
            rootVal = postorder.pop()
            root = TreeNode(rootVal)

            leftInorder = []
            leftPostorder = []
            while inorder and inorder[0] != rootVal:
                leftInorder.append(inorder.pop(0))
                leftPostorder.append(postorder.pop(0))
            inorder.pop(0)
            root.left = recur(leftInorder, leftPostorder)
            root.right = recur(inorder, postorder)
            return root
        return recur(inorder, postorder)

# @lc code=end

