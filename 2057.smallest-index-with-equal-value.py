#
# @lc app=leetcode id=2057 lang=python3
#
# [2057] Smallest Index With Equal Value
#

# @lc code=start
class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        for idx, val in enumerate(nums):
            if idx%10 == val:
                return idx
        return -1
# @lc code=end

