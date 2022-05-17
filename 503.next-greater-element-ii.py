#
# @lc app=leetcode id=503 lang=python3
#
# [503] Next Greater Element II
#

# @lc code=start

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = [] #(idx, val) decreasing stack
        n = len(nums)
        res = [-1]*n
        for idx, num in enumerate(nums):
            while stack and stack[-1][0] < num:
                prev_idx = stack.pop()[0]
                res[prev_idx] = num
            stack.append((idx, num))
        return res
# @lc code=end

