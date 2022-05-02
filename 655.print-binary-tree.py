#
# @lc app=leetcode id=655 lang=python3
#
# [655] Print Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        res = []
        if not root:
            return res
        def height(root):
            if not root:
                return -1
            return max(height(root.left), height(root.right)) + 1
        h = height(root)
        n = 2**(h+1) - 1
        q = [(root, 0, (n-1)//2)]
        res = [["" for _ in range(n)] for _ in range(h+1)]
        while q:
            node, r, c = q.pop()
            res[r][c] = str(node.val)
            if node.left:
                q.append((node.left, r+1, c-2**(h-r-1)))
            if node.right:
                q.append((node.right, r+1, c+2**(h-r-1)))
        return res
            
# @lc code=end

