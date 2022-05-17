#
# @lc app=leetcode id=1209 lang=python3
#
# [1209] Remove All Adjacent Duplicates in String II
#

# @lc code=start
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for ch in s:
            if not stack:
                stack.append([ch,1])
            elif stack[-1][0] == ch:
                stack[-1][1] += 1
                if stack[-1][1] >= k:
                    stack[-1][1] -= k
                if stack[-1][1] == 0:
                    stack.pop()
            else:
                stack.append([ch, 1])
        new_string = ''
        for ch, count in stack:
            new_string += ch*count
        return new_string
# @lc code=end

