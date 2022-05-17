#
# @lc app=leetcode id=783 lang=python3
#
# [783] Minimum Distance Between BST Nodes
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        result = float('inf')
        prev = None
        node = root
        def find_ped(node):
            curr = node.left
            while curr and curr.right and curr.right!=node:
                curr = curr.right
            return curr
        while node:
            if not node.left:
                curr = node
                node = node.right
            else:
                ped = find_ped(node)
                if ped.right == node:
                    curr = node
                    ped.right = None
                    node = node.right
                else:
                    ped.right = node
                    node = node.left
                    continue
            if prev:
                result = min(result, abs(curr.val-prev.val))
            prev = curr
        return result



# @lc code=end

