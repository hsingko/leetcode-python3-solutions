#
# @lc app=leetcode id=1800 lang=python3
#
# [1800] Maximum Ascending Subarray Sum
#

# @lc code=start
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        ans = 0
        curr = 0
        for idx, val in enumerate(nums):
            if idx == 0 or val > nums[idx-1]:
                curr += val
            else:
                ans = max(curr, ans)
                curr = val
        return max(ans, curr)
# @lc code=end

