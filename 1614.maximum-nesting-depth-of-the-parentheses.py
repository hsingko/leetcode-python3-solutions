#
# @lc app=leetcode id=1614 lang=python3
#
# [1614] Maximum Nesting Depth of the Parentheses
#

# @lc code=start
class Solution:
    def maxDepth(self, s: str) -> int:
        result = 0
        stack = []
        for ch in s:
            if ch == ')':
                curr = 0
                while stack[-1] != '(':
                    curr = max(curr, int(stack.pop()))
                stack.pop()
                stack.append(curr+1)
            elif ch == '(':
                stack.append(ch)
        return max(stack) if stack else 0
# @lc code=end

