#
# @lc app=leetcode id=747 lang=python3
#
# [747] Largest Number At Least Twice of Others
#

# @lc code=start
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        M = max(nums)
        indice = -1
        for idx, val in enumerate(nums):
            if val == M:
                indice = idx
            elif val*2 > M:
                return -1
        return indice


# @lc code=end

