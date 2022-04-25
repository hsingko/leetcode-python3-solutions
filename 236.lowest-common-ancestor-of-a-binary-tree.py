#
# @lc app=leetcode id=236 lang=python3
#
# [236] Lowest Common Ancestor of a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parent = {root: None}
        stack = [root]
        while stack:
            curr = stack.pop()
            if curr.left:
                parent[curr.left] = curr
                stack.append(curr.left)
            if curr.right:
                parent[curr.right] = curr
                stack.append(curr.right)
        path_p = []
        while p:
            path_p.append(p)
            p = parent[p]
        path_q = set()
        while q:
            path_q.add(q)
            q = parent[q]

        for k in path_p:
            if k in path_q:
                return k
        return None

# @lc code=end

