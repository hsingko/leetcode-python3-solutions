#
# @lc app=leetcode id=674 lang=python3
#
# [674] Longest Continuous Increasing Subsequence
#

# @lc code=start
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        n = len(nums)
        p = 0
        ans = 0
        while p < n:
            q = p 
            while q + 1 < n and nums[q+1] > nums[q]:
                q += 1
            ans = max(q-p+1, ans)
            p = q + 1
        return ans
# @lc code=end

