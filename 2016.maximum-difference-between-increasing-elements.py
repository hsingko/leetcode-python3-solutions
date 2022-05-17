#
# @lc app=leetcode id=2016 lang=python3
#
# [2016] Maximum Difference Between Increasing Elements
#

# @lc code=start
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        minimal = nums[0]
        ans = -1
        for num in nums[1:]:
            minimal = min(minimal, num)
            ans = max(ans, num-minimal)
        return ans if ans else -1
# @lc code=end

