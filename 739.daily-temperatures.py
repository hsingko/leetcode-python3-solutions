#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#

# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # (idx, val) decreasing stack
        n = len(temperatures)
        ans = [0]*n
        for idx, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                index = stack.pop()[0]
                ans[index] = idx - index
            stack.append((idx, temp))
        return ans
# @lc code=end

