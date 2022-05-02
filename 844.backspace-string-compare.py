#
# @lc app=leetcode id=844 lang=python3
#
# [844] Backspace String Compare
#

# @lc code=start
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def gen(string):
            stack = []
            for ch in string:
                if ch == '#':
                    if stack:
                        stack.pop()
                else:
                    stack.append(ch)
            return ''.join(stack)
        return gen(s) == gen(t)

# @lc code=end

