#
# @lc app=leetcode id=896 lang=python3
#
# [896] Monotonic Array
#

# @lc code=start
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        d = list(map(lambda x:x[0]-x[1], zip(nums[1:], nums)))
        return all(map(lambda x:x<=0, d)) or all(map(lambda x:x>=0, d))
# @lc code=end

