#
# @lc app=leetcode id=1848 lang=python3
#
# [1848] Minimum Distance to the Target Element
#

# @lc code=start
class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        step = 1
        if nums[start] == target:
            return 0
        n = len(nums)
        while step + start < n or start - step > -1:
            if step + start < n and nums[step+start] == target:
                return step
            if start - step > -1 and nums[start-step] == target:
                return step
            step += 1
        return -1

# @lc code=end

